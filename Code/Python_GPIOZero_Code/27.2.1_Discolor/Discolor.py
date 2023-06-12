#!/usr/bin/env python3
#############################################################################
# Filename    : TouchSensor.py
# Description : Touch Sensor TTP223 Control LED brightness.
# Author      : www.freenove.com
# modification: 2023/05/13
#####################PW###################################################
from gpiozero import RGBLED
from sensor import TouchSensor
import time

sensorPin = 18     # define sensorPin
sensor = TouchSensor(sensorPin, pull_up=False)
led = RGBLED(red=22, green=27, blue=17,active_high=False) # define the pins for R:GPIO22,G:GPIO27,B:GPIO17
grade=0

# Define the functions that will be called when the line is
def SensorEvent(): # When Sensor is pressed, this function will be executed
    global  grade
    grade=grade+1
    print("Sensor is pressed!")
    if(grade > 3):
        grade=0
 
def loop():
    sensor.when_no_touch = SensorEvent
    while True:
        global grade
        if grade==1:
            led.color = (1, 0, 0)
            print ('The current color is red')
        elif grade==2:
            led.color = (0, 1, 0)          
            print ('The current color is green')
        elif grade==3:
            led.color = (0, 0, 1) 
            print ('The current color is blue')
        else:
            led.off()
            print ('Close the RGBLED')
        time.sleep(0.001)

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