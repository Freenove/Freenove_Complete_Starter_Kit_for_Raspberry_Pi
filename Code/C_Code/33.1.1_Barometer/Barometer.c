/**********************************************************************
* Filename    : Barometer.c
* Description : Read atmospheric pressure, temperature and current altitude of BMP180 pressure sensor.
* Author      : www.freenove.com
* modification: 2022/4/20
**********************************************************************/
#include <stdio.h>
#include <stdint.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <linux/i2c-dev.h>
#include <linux/i2c.h>
#include <sys/ioctl.h>
#include "smbus.h" 
#include <math.h>

#define bmp180_I2C_ADDRESS 0x77
const unsigned char bmp180_OVERSAMPLING_SETTING = 3;

// Calibration values - These are stored in the BMP180
short int ac1;
short int ac2; 
short int ac3; 
unsigned short int ac4;
unsigned short int ac5;
unsigned short int ac6;
short int b1; 
short int b2;
short int mb;
short int mc;
short int md;
int b5; 
unsigned int temperature, pressure, altitude;

// Open a connection to the bmp180
// Returns a file id
int bmp180_i2c_Begin(){
    int fd;
    char *fileName = "/dev/i2c-1";
    // Open port for reading and writing
    if ((fd = open(fileName, O_RDWR)) < 0)
        exit(1);
    // Set the port options and set the address of the device
if (ioctl(fd, I2C_SLAVE, bmp180_I2C_ADDRESS) < 0){
        close(fd);
        exit(1);
    }
    return fd;
}
    // Read two words from the bmp180 and supply it as a 16 bit integer
__s32 bmp180_i2c_Read_Int(int fd, __u8 address){
    __s32 res = i2c_smbus_read_word_data(fd, address);
    if (res < 0){
    	    close(fd);
        exit(1);
    }
    // Convert result to 16 bits and swap bytes
    res = ((res<<8) & 0xFF00) | ((res>>8) & 0xFF);
    return res;
}
    //Write a byte to the bmp180
void bmp180_i2c_Write_Byte(int fd, __u8 address, __u8 value){
    if (i2c_smbus_write_byte_data(fd, address, value) < 0) {
        close(fd);
        exit(1);
    }
}
    // Read a block of data bmp180
void bmp180_i2c_Read_Block(int fd, __u8 address, __u8 length, __u8 *values){
    if(i2c_smbus_read_i2c_block_data(fd, address,length,values)<0){
        	close(fd);
        exit(1);
    }
}
void bmp180_Calibration(){
    int fd = bmp180_i2c_Begin();
    ac1 = bmp180_i2c_Read_Int(fd,0xAA);
    ac2 = bmp180_i2c_Read_Int(fd,0xAC);
    ac3 = bmp180_i2c_Read_Int(fd,0xAE);
    ac4 = bmp180_i2c_Read_Int(fd,0xB0);
    ac5 = bmp180_i2c_Read_Int(fd,0xB2);
    ac6 = bmp180_i2c_Read_Int(fd,0xB4);
    b1 = bmp180_i2c_Read_Int(fd,0xB6);
    b2 = bmp180_i2c_Read_Int(fd,0xB8);
    mb = bmp180_i2c_Read_Int(fd,0xBA);
    mc = bmp180_i2c_Read_Int(fd,0xBC);
    md = bmp180_i2c_Read_Int(fd,0xBE);
    close(fd);
}
    // Read the uncompensated temperature value
unsigned int bmp180_ReadUT(){
    unsigned int ut = 0;
    int fd = bmp180_i2c_Begin();
    // Write 0x2E into Register 0xF4
    // This requests a temperature reading
    bmp180_i2c_Write_Byte(fd,0xF4,0x2E);
    // Wait at least 5ms
    usleep(5000);
    // Read the two byte result from address 0xF6
    ut = bmp180_i2c_Read_Int(fd,0xF6);
    // Close the i2c file
    close (fd);
    return ut;
}
// Read the uncompensated pressure value
unsigned int bmp180_ReadUP(){
    unsigned int up = 0;
    int fd = bmp180_i2c_Begin();
    // Write 0x34+(bmp180_OVERSAMPLING_SETTING<<6) into register 0xF4
    // Request a pressure reading w/ oversampling setting
    bmp180_i2c_Write_Byte(fd,0xF4,0x34 + (bmp180_OVERSAMPLING_SETTING<<6));
    // Wait for conversion, delay time dependent on oversampling setting·
    usleep((2 + (3<<bmp180_OVERSAMPLING_SETTING)) * 1000);
    // Read the three byte result from 0xF6
    // 0xF6 = MSB, 0xF7 = LSB and 0xF8 = XLSB
    __u8 values[3];
    bmp180_i2c_Read_Block(fd, 0xF6, 3, values);
    up = (((unsigned int) values[0] << 16) | ((unsigned int) values[1] << 8) | (unsigned int) values[2]) >> (8-bmp180_OVERSAMPLING_SETTING);
    return up;
}
// Calculate pressure given uncalibrated pressure
unsigned int bmp180_GetPressure(unsigned int up){
    int x1, x2, x3, b3, b6, p;
    unsigned int b4, b7;
    b6 = b5 - 4000;
    // Calculate B3
    x1 = (b2 * (b6 * b6)>>12)>>11;
    x2 = (ac2 * b6)>>11;
    x3 = x1 + x2;
    b3 = (((((int)ac1)*4 + x3)<<bmp180_OVERSAMPLING_SETTING) + 2)>>2;
    // Calculate B4
    x1 = (ac3 * b6)>>13;
    x2 = (b1 * ((b6 * b6)>>12))>>16;
    x3 = ((x1 + x2) + 2)>>2;
    b4 = (ac4 * (unsigned int)(x3 + 32768))>>15;
    b7 = ((unsigned int)(up - b3) * (50000>>bmp180_OVERSAMPLING_SETTING));
    if (b7 < 0x80000000)
        p = (b7<<1)/b4;
    else
        p = (b7/b4)<<1;
    x1 = (p>>8) * (p>>8);
    x1 = (x1 * 3038)>>16;
    x2 = (-7357 * p)>>16;
    p += (x1 + x2 + 3791)>>4;
    return p;
}
// Calculate temperature given uncalibrated temperature
// Value returned will be in units of 0.1 deg C
unsigned int bmp180_GetTemperature(unsigned int ut){
    int x1, x2;
    x1 = (((int)ut - (int)ac6)*(int)ac5) >> 15;
    x2 = ((int)mc << 11)/(x1 + md);
    b5 = x1 + x2;
    unsigned int result = ((b5 + 8)>>4);  
    return result;
}
// Arduino library.  The number divided into pressure for
// float A is derived from the local pressure as explained
// at http://learn.adafruit.com/bmp180/using-the-bmp180.
unsigned int bmp180_Altitude(float pressure){
    float A = pressure/101325.0;
    float B = 1/5.25588;
    float C = pow(A,B);
    C = 1 - C;
    C = C / 0.0000225577;
    return C;
}
int main(int argc, char **argv){
    printf("Program is starting ... \n");
    while(1){
        bmp180_Calibration();
        temperature = bmp180_GetTemperature(bmp180_ReadUT());
        pressure = bmp180_GetPressure(bmp180_ReadUP());
        altitude = bmp180_Altitude(pressure);
        printf("Temperature\t%0.1f ℃\n", ((double)temperature)/10);
        printf("Pressure\t%0.2f hPa\n", ((double)pressure)/100);
        printf("Altitude\t%0.1f m\n\n", (double)altitude);
        usleep(2000*1000);
    }
    return 0;
}
