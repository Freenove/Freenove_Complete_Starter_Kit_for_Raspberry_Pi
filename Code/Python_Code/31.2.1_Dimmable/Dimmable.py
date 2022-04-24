#!/usr/bin/env python3
#############################################################################
# Filename    : Dimmable.py
# Description : Use rotary encoder to control LED brightness. 
# Author      : www.freenove.com
# modification: 2022/4/20
########################################################################
import RPi.GPIO as GPIO
import time

clkPin = 11    # define clkPin
dtPin = 12     # define dtPin
swPin = 13     # define swPin
ledPin = 15    # define ledPin

previousCounterValue = 0
symbol = 0
lastDTStatus = 0
currentDTStatus = 0

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)      # Use PHYSICAL GPIO Numbering
    GPIO.setwarnings(False)
    GPIO.setup(ledPin,GPIO.OUT)   # Set ledPin to OUTPUT mode,
    GPIO.setup(clkPin, GPIO.IN)   # Set clkPin to INPUT mode,
    GPIO.setup(dtPin, GPIO.IN)    # Set dtPin to INPUT mode,
    GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set swPin to INPUT mode, and pull up to HIGH level
    p = GPIO.PWM(ledPin,1000)
    p.start(0)

def rotaryDeal():
    global symbol
    global lastDTStatus
    global currentDTStatus
    global previousCounterValue
    lastDTStatus = GPIO.input(dtPin)  
    while(not GPIO.input(clkPin)):      #未旋转时，GPIO.input(CLKPin)值为1，旋转时会变为0
        currentDTStatus = GPIO.input(dtPin)  #记录旋转时的当前值
        symbol = 1
    if symbol == 1:
        symbol = 0
        if (lastDTStatus == 1) and (currentDTStatus == 0): #顺时针旋转，角位移增大，计数值增大
            previousCounterValue = previousCounterValue + 1 
        if (lastDTStatus == 0) and (currentDTStatus == 1): #逆时针旋转，角位移减少，计数值减少
            previousCounterValue = previousCounterValue - 1 

def sensorEvent(channel):
    global previousCounterValue
    previousCounterValue = 0
    p.ChangeDutyCycle(0)        # Mapping to PWM duty cycle
def loop():
    global previousCounterValue
    currentCounterValue = 0 

    GPIO.add_event_detect(swPin, GPIO.FALLING, callback=sensorEvent)   #当按下按钮时，调用回调函数sensorEvent
    while True:
        rotaryDeal()
        if previousCounterValue>=100:
            previousCounterValue=100
        if previousCounterValue<=0:
            previousCounterValue=0 
        if currentCounterValue != previousCounterValue:
            print('Counter = %d' % previousCounterValue)
            currentCounterValue = previousCounterValue
        p.ChangeDutyCycle(previousCounterValue)        # Mapping to PWM duty cycle

def destroy():
    GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program start from here
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
