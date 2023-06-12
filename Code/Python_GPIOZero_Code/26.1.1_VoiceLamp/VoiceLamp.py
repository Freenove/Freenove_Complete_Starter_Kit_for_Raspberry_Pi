#!/usr/bin/env python3
########################################################################
# Filename    : VoiceLamp.py
# Description : Make sound control lamp with high-sensitivity microphone sensor. 
# Author      : www.freenove.com
# modification: 2023/05/13
########################################################################
from gpiozero import LED
from sensor import MicrophoneSensor
import time

ledPin    = 17    # define ledPin
sensorPin = 18    # define sensorPin
led    = LED(ledPin)    
sensor=MicrophoneSensor(sensorPin, pull_up=False)

def loop():
    while True:
       if sensor.is_active:
           led.on()                    # turn on led
           time.sleep(5)
           led.off()                   # turn off led
           print ('led turned on >>>') # print information on termina
       else:
           led.off()
           print ('led turned off >>>')

def destroy():
    led.close() 
    sensor.close()                     

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        print("Ending program")