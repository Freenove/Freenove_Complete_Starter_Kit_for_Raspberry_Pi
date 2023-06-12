#!/usr/bin/env python3
#############################################################################
# Filename    : PhotoSensor.py
# Description : U-shaped photoelectric sensor control LED.
# Author      : www.freenove.com
# modification: 2023/05/13
########################################################################
from gpiozero import LED
from sensor import PhotoSensor
import time

ledPin    = 17
sensorPin = 18     # define sensorPin
sensor = PhotoSensor(sensorPin, pull_up=False)
led = LED(ledPin, initial_value=True) 

# Define the functions that will be called when the line is
def SensorEvent1(channel): # The sensor is blocked
    led.on()
    print ('When the sensor is not blocked, led turned on >>>')     # print information on terminal
def SensorEvent2(channel): # The sensor is blocked
    led.off()   
    print (' When the sensor is blocked, led turned off <<<')
 
def loop():
    sensor.when_occlusion = SensorEvent1
    sensor.when_no_occlusion = SensorEvent2
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