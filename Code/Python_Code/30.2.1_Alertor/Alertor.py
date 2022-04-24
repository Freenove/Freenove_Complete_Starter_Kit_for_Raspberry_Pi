#!/usr/bin/env python3
#############################################################################
# Filename    : Alertor.py
# Description : Make a sound and light reminder with a buzzer and infrared obstacle avoidance sensor.
# Author      : www.freenove.com
# modification: 2022/4/20
########################################################################
import RPi.GPIO as GPIO
import time
ledPin = 13       # define ledPin
sensorPin = 12    # define buttonPin
buzzerPin = 11    # define buzzerPin

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)         # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)     # set ledPin to OUTPUT mode
    GPIO.setup(buzzerPin, GPIO.OUT)   # set buzzerPin to OUTPUT mode
    GPIO.setup(sensorPin, GPIO.IN)     # set sensorPin to INPUT mode

def alarm():
    times=3
    while times:
        GPIO.output(buzzerPin,GPIO.HIGH) # turn on buzzer
        GPIO.output(ledPin,GPIO.HIGH)    # turn on led
        time.sleep(0.05)
        GPIO.output(buzzerPin,GPIO.LOW)  # turn off buzzer
        GPIO.output(ledPin,GPIO.LOW)     # turn on led
        time.sleep(0.05)
        times-=1

def sensorEvent(channel): # When sensor is blocked, this function will be executed
    alarm()
    
def loop():
    GPIO.add_event_detect(sensorPin,GPIO.FALLING,callback = sensorEvent,bouncetime=300)
    while True:
        pass
def destroy():
    GPIO.cleanup()             # Release GPIO resource
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
