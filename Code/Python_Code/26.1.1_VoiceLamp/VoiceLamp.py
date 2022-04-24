#!/usr/bin/env python3
########################################################################
# Filename    : VoiceLamp.py
# Description : Make sound control lamp with high-sensitivity microphone sensor. 
# Author      : www.freenove.com
# modification: 2021/4/20
########################################################################
import RPi.GPIO as GPIO
import time

ledPin = 11    # define ledPin
sensorPin = 12    # define bsensorPin

def setup():
    GPIO.setmode(GPIO.BOARD)          # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)      # set ledPin to OUTPUT mode
    GPIO.setup(sensorPin, GPIO.IN)    # set sensorPin to INPUT mode

def loop():
    while True:
        if GPIO.input(sensorPin)==GPIO.HIGH: # The sensor is blocked
            GPIO.output(ledPin,GPIO.HIGH)    # turn on led
            time.sleep(5)
            GPIO.output(ledPin,GPIO.LOW)
            print ('led turned on >>>')     # print information on terminal
        else : #  The sensor is not blocked
            GPIO.output(ledPin,GPIO.LOW) # turn off led	
            print ('led turned off <<<')

def destroy(): 
    GPIO.cleanup()                     # Release GPIO resource

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
