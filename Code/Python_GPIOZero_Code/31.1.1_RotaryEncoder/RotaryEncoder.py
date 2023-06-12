#!/usr/bin/env python3
#############################################################################
# Filename    : RotaryEncoder.py
# Description : Use rotary encoder to make a simple counter. 
# Author      : www.freenove.com
# modification: 2023/05/15
########################################################################
from gpiozero import DigitalInputDevice,Button
import time

clkPin = 17     # define the clkPin
dtPin  = 18     # define the dtPin
swPin  = 27     # define the swPin

previousCounterValue = 0
symbol = 0
lastDTStatus = 0
currentDTStatus = 0

clk = DigitalInputDevice(clkPin)  
dt  = DigitalInputDevice(dtPin)    
sw  = Button(swPin,pull_up=True)     

def rotaryDeal():
    global symbol
    global lastDTStatus
    global currentDTStatus
    global previousCounterValue
    lastDTStatus = dt.value
    while(not clk.value):     # clk.value is 1 when not rotated and becomes 0 when rotated
        currentDTStatus = dt.value  # Record the current value of the rotation
        symbol = 1
    if symbol == 1:
        symbol = 0
        if (lastDTStatus == 1) and (currentDTStatus == 0): # Rotate clockwise, the angular displacement increases, and the count value increases
            previousCounterValue = previousCounterValue + 1 
        if (lastDTStatus == 0) and (currentDTStatus == 1): # Counterclockwise rotation, angular displacement reduction, count value reduction
            previousCounterValue = previousCounterValue - 1  

def sensorEvent():
    global previousCounterValue
    previousCounterValue = 0

def loop():
    global previousCounterValue
    currentCounterValue = 0 
    sw.when_pressed = sensorEvent
    while True:
        rotaryDeal()
        
        if currentCounterValue != previousCounterValue:
            print('Counter = ' ,previousCounterValue)
            currentCounterValue = previousCounterValue

def destroy():
    clk.close()
    dt.close()  
    sw.close()   

if __name__ == '__main__':     # Program start from here
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
        print("Ending program")
