#!/usr/bin/env python3
########################################################################
# Filename    : RainbowLight.py
# Description : Use freenve 8RGB LED module to achieve rainbow lights.
# Author      : www.freenove.com
# modification: 2023/05/13
########################################################################
# -*-coding: utf-8 -*-
import time
from rpi_ws281x import *
from ADCDevice import *
# LED strip configuration:
LED_COUNT      = 8      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
# Define functions which animate LEDs in various ways.
class Led:
    def __init__(self):
        #Control the sending order of color data
        self.ORDER = "RGB"  
        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()
        
        self.adc = ADCDevice(0x4b) # Define an ADCDevice class object
        if(self.adc.detectI2C(0x4b)):
            self.adc = ADS7830(0x4b)
        elif(adc.detectI2C(0x48)):  # Detect the pcf8591.
            self.adc = PCF8591()
        else:
            print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n");
            exit(-1)
    
    def HSL_RGB(self,degree):
        degree=degree/360*255
        if degree < 85:
            red = 255 - degree * 3
            green = degree * 3
            blue = 0
        elif degree < 170:
            degree = degree - 85
            red = 0
            green = 255 - degree * 3
            blue = degree * 3
        else:
            degree = degree - 170
            red = degree * 3
            green = 0
            blue = 255 - degree * 3
        return int(red),int(green),int(blue)
led=Led()                 
# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        while True:
            for i in range(8):
                value = round(led.adc.analogRead(2) / 255.0 * 360+i*45)    # read the ADC value of channel 2
                if value > 360 :
                    value = value-360
                red,green,blue=led.HSL_RGB(value)
                led.strip.setPixelColor(i, Color(red,green,blue))
            time.sleep(0.1)
            led.strip.show()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        led.adc.close()
        for i in range(8):
            led.strip.setPixelColor(i, Color(0,0,0))
        led.strip.show()
