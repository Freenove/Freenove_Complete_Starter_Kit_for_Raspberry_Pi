#!/usr/bin/env python3
#############################################################################
# Filename    : RotaryEncoder.py
# Description : Read atmospheric pressure, temperature and current altitude of BMP180 pressure sensor.
# Author      : www.freenove.com
# modification: 2022/4/20
########################################################################
import time
import smbus

# BMP180 default address.
BMP180_I2CADDR = 0x77

# Operating Modes
BMP180_ULTRALOWPOWER = 0
BMP180_STANDARD = 1
BMP180_HIGHRES = 2
BMP180_ULTRAHIGHRES = 3

# BMP180 Registers
BMP180_AC1 = 0xAA  #    Calibration data (16 bits)
BMP180_AC2 = 0xAC  #    Calibration data (16 bits)
BMP180_AC3 = 0xAE  #    Calibration data (16 bits)
BMP180_AC4 = 0xB0  #    Calibration data (16 bits)
BMP180_AC5 = 0xB2  #    Calibration data (16 bits)
BMP180_AC6 = 0xB4  #    Calibration data (16 bits)
BMP180_B1 = 0xB6   #    Calibration data (16 bits)
BMP180_B2 = 0xB8   #    Calibration data (16 bits)
BMP180_MB = 0xBA   #    Calibration data (16 bits)
BMP180_MC = 0xBC   #    Calibration data (16 bits)
BMP180_MD = 0xBE   #    Calibration data (16 bits)
BMP180_CONTROL = 0xF4
BMP180_TEMPDATA = 0xF6
BMP180_PRESSUREDATA = 0xF6

# Commands
BMP180_READTEMPCMD = 0x2E
BMP180_READPRESSURECMD = 0x34

class BMP180(object):
    def __init__(self, address=BMP180_I2CADDR, mode=BMP180_ULTRAHIGHRES):
        self._mode = mode
        self._address = address
        self._bus = smbus.SMBus(1)
        # Load calibration values.
        self._load_calibration()
        # Kalman Filter
        self._x_last = 0
        self._p_last = 0
    def _read_byte(self, cmd):
        return self._bus.read_byte_data(self._address, cmd)
    def _read_u16(self, cmd):
        MSB = self._bus.read_byte_data(self._address, cmd)
        LSB = self._bus.read_byte_data(self._address, cmd + 1)
        return (MSB << 8) + LSB
    def _read_s16(self, cmd):
        result = self._read_u16(cmd)
        if result > 32767: result -= 65536
        return result
    def _write_byte(self, cmd, val):
        self._bus.write_byte_data(self._address, cmd, val)
    def _load_calibration(self):
        "load calibration"
        self.AC1 = self._read_s16(BMP180_AC1)  # INT16
        self.AC2 = self._read_s16(BMP180_AC2)  # INT16
        self.AC3 = self._read_s16(BMP180_AC3)  # INT16
        self.AC4 = self._read_u16(BMP180_AC4)  # UINT16
        self.AC5 = self._read_u16(BMP180_AC5)  # UINT16
        self.AC6 = self._read_u16(BMP180_AC6)  # UINT16
        self.B1 = self._read_s16(BMP180_B1)  # INT16
        self.B2 = self._read_s16(BMP180_B2)  # INT16
        self.MB = self._read_s16(BMP180_MB)  # INT16
        self.MC = self._read_s16(BMP180_MC)  # INT16
        self.MD = self._read_s16(BMP180_MD)  # INT16
    def read_raw_temp(self):
        """Reads the raw (uncompensated) temperature from the sensor."""
        self._write_byte(BMP180_CONTROL, BMP180_READTEMPCMD)
        time.sleep(0.005)  # Wait 5ms
        raw = self._read_u16(BMP180_TEMPDATA)
        return raw
    def read_raw_pressure(self):
        """Reads the raw (uncompensated) pressure level from the sensor."""
        self._write_byte(BMP180_CONTROL, BMP180_READPRESSURECMD + (self._mode << 6))
        if self._mode == BMP180_ULTRALOWPOWER:
            time.sleep(0.005)
        elif self._mode == BMP180_HIGHRES:
            time.sleep(0.014)
        elif self._mode == BMP180_ULTRAHIGHRES:
            time.sleep(0.026)
        else:
            time.sleep(0.008)
        MSB = self._read_byte(BMP180_PRESSUREDATA)
        LSB = self._read_byte(BMP180_PRESSUREDATA + 1)
        XLSB = self._read_byte(BMP180_PRESSUREDATA + 2)
        raw = ((MSB << 16) + (LSB << 8) + XLSB) >> (8 - self._mode)
        return raw
    def read_temperature(self):
        UT = self.read_raw_temp()
        X1 = ((UT - self.AC6) * self.AC5) >> 15
        X2 = (self.MC << 11) // (X1 + self.MD)
        B5 = X1 + X2
        temp = ((B5 + 8) >> 4) / 10.0
        return temp
    def read_pressure(self):
        UT = self.read_raw_temp()
        UP = self.read_raw_pressure()
        X1 = ((UT - self.AC6) * self.AC5) >> 15
        X2 = (self.MC << 11) // (X1 + self.MD)
        B5 = X1 + X2
        # Pressure Calculations
        B6 = B5 - 4000
        X1 = (self.B2 * (B6 * B6) >> 12) >> 11
        X2 = (self.AC2 * B6) >> 11
        X3 = X1 + X2
        B3 = (((self.AC1 * 4 + X3) << self._mode) + 2) // 4
        X1 = (self.AC3 * B6) >> 13
        X2 = (self.B1 * ((B6 * B6) >> 12)) >> 16
        X3 = ((X1 + X2) + 2) >> 2
        B4 = (self.AC4 * (X3 + 32768)) >> 15
        B7 = (UP - B3) * (50000 >> self._mode)
        if B7 < 0x80000000:
            p = (B7 * 2) // B4
        else:
            p = (B7 // B4) * 2
        X1 = (p >> 8) * (p >> 8)
        X1 = (X1 * 3038) >> 16
        X2 = (-7357 * p) >> 16
        p = p + ((X1 + X2 + 3791) >> 4)
        return p
    def read_altitude(self, local_pa=101325.0, sealevel_pa=101325.0):
        pressure = float(local_pa)
        altitude = 44330.0 * (1.0 - pow(pressure / sealevel_pa, (1.0 / 5.255)))
        return altitude
    def read_sealevel_pressure(self, local_pa=101325.0, altitude_m=0.0):
        pressure = float(local_pa)
        p0 = pressure / pow(1.0 - altitude_m / 44330.0, 5.255)
        return p0
if __name__ == '__main__':
    bmp = BMP180()
    while (True):
            temp = bmp.read_temperature()
            pressure=bmp.read_pressure()
            altitude = bmp.read_altitude(pressure)
            print("Temperature:%.1f ℃" %temp)
            print("Pressure:%.2fhPa" %(pressure / 100.0))
            print("Altitude:%.2fm" %altitude)
            print()
            time.sleep(2)
