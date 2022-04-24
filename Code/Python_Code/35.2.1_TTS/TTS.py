#!/usr/bin/env python3
#############################################################################
# Filename    : TTS.py
# Description : Make TTS alerts using the speaker amplifier module PAM8403.  
# Author      : www.freenove.com
# modification: 2022/4/20
########################################################################
import RPi.GPIO as GPIO
import os

sensorPin = 12    # define sensorPin

def setup():
    GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
    GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set sensorPin to PULL UP INPUT mode

def loop():
    while True:
        if GPIO.input(sensorPin)==GPIO.LOW:
            os.system("espeak 'Hello, please  stay away'")

def destroy():
    GPIO.cleanup()                    # Release GPIO resource

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
