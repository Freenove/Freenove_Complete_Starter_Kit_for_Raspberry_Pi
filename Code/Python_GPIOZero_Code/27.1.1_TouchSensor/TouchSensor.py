#!/usr/bin/env python3
#############################################################################
# Filename    : TouchSensor.py
# Description : Touch Sensor TTP223 Control LED brightness.
# Author      : www.freenove.com
# modification: 2023/05/13
#####################PW###################################################
from gpiozero import PWMLED
from sensor import TouchSensor
import time

ledPin    = 17     # define ledPin
sensorPin = 18     # define sensorPin
led    = PWMLED(ledPin)    
sensor = TouchSensor(sensorPin, pull_up=False)
grade=0

# Define the functions that will be called when the line is
def SensorEvent():
    global  grade
    grade=grade+1
    print("Sensor is pressed!")
    if(grade > 3):
        grade=0

def loop():
    sensor.when_touch = SensorEvent
    while True:
        global grade
        if grade==1:
            dc=35
            led.value = dc / 100.0     # set dc value as the duty cycle
        elif grade==2:
            dc=65
            led.value = dc / 100.0     # set dc value as the duty cycle
        elif grade==3:
            dc=100
            led.value = dc / 100.0     # set dc value as the duty cycle
        else :
            dc=0
            led.value = dc / 100.0     # set dc value as the duty cycle

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