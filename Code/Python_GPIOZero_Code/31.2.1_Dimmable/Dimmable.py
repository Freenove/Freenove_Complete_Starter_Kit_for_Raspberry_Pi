#!/usr/bin/env python3
#############################################################################
# Filename    : Dimmable.py
# Description : Use rotary encoder to control LED brightness. 
# Author      : www.freenove.com
# modification: 2023/05/15
########################################################################
from gpiozero import DigitalInputDevice,Button,PWMLED
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
led = PWMLED(22)

def rotaryDeal():
    global symbol
    global lastDTStatus
    global currentDTStatus
    global previousCounterValue
    lastDTStatus = dt.value
    while(not clk.value):      # When not rotating, the value of clk.value is 1, and it will become 0 when rotating.
        currentDTStatus = dt.value  # Record the current value of the rotation
        symbol = 1
    if symbol == 1:
        symbol = 0
        if (lastDTStatus == 1) and (currentDTStatus == 0): #When rotate clockwise, the angular displacement increases, and the count value increases.
            previousCounterValue = previousCounterValue + 1 
        if (lastDTStatus == 0) and (currentDTStatus == 1): #When rotate counterclockwise, the angular displacement decreases, and the count value decreases.
            previousCounterValue = previousCounterValue - 1  

def sensorEvent(channel):
    global previousCounterValue
    previousCounterValue = 0

def loop():
    global previousCounterValue
    currentCounterValue = 0 
    sw.when_pressed = sensorEvent
    while True:
        rotaryDeal()
        if previousCounterValue>=100:
            previousCounterValue=100
        if previousCounterValue<=0:
            previousCounterValue=0 
        if currentCounterValue != previousCounterValue:
            print('Counter = %d' % previousCounterValue)
            currentCounterValue = previousCounterValue
        led.value = previousCounterValue / 100.0     # set dc value as the duty cycle

def destroy():
    clk.close()
    dt.close()  
    sw.close()   

if __name__ == '__main__':     # Program start from here
    print ('Program is starting ... ')
#     setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
        print("Ending program")