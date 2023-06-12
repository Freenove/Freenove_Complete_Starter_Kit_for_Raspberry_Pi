#!/usr/bin/env python3
#############################################################################
# Filename    : HallSensor.py
# Description : Hall sensor control LED.
# Author      : www.freenove.com
# modification: 2022/4/20
########################################################################
from gpiozero import LED
from sensor import HallSensor
import time

ledPin    = 17
sensorPin = 18     # define sensorPin
sensor = HallSensor(sensorPin, pull_up=False)
led = LED(ledPin, initial_value=False) 

# Define the functions that will be called when the line is
def SensorEvent1(channel): # The sensor is blocked
    led.on()
    print ('led turned on >>>')     # print information on terminal
def SensorEvent2(channel): # The sensor is blocked
    led.off()   
    print ('led turned off >>>')     # print information on terminal
 
def loop():
    sensor.when_magnetic_field = SensorEvent1
    sensor.when_no_magnetic_field = SensorEvent2
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