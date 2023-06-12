#!/usr/bin/env python3
########################################################################
# Filename    : Ledpixel.py
# Description : Use freenve 8RGB LED module to achieve a flowing light.
# Author      : www.freenove.com
# modification: 2023/05/13
########################################################################
# -*-coding: utf-8 -*-
import time
from rpi_ws281x import *
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
        #self.strip.setPixelColor(i, color)
        #self.strip.show()
led=Led()                 
# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    col=[Color(255,0,0),Color(0,255,0),Color(0,0,255)]
    try:
        while True:
            for c in range(3):
                for i in range(8):
                    led.strip.setPixelColor(i,col[c])
                    time.sleep(0.1)
                    led.strip.show()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        for i in range(8):
            led.strip.setPixelColor(i, Color(0,0,0))
        led.strip.show()
