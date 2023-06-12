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
    sensor.when_sound = lambda: led.blink(on_time=5, off_time=0, n=1)
    while True:
        time.sleep(1)

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