#!/usr/bin/env python3
#############################################################################
# Filename    : Dimmable.py
# Description : Use rotary encoder to control LED brightness. 
# Author      : www.freenove.com
# modification: 2023/05/15
########################################################################
from gpiozero import RotaryEncoder,Button,PWMLED
import time
CounterValue = 0 
NextCounterValue = 0
button = Button(27) # define Button pin according to BCM Numbering    
rotor = RotaryEncoder(17, 18,max_steps=30)
led = PWMLED(22)

def forward():
    global CounterValue
    CounterValue =CounterValue+1

def reverse():
    global CounterValue
    CounterValue =CounterValue-1
def reset():
    global CounterValue
    CounterValue =0

def loop():
    global CounterValue
    global NextCounterValue
    button.when_pressed = reset
    rotor.when_rotated_clockwise = forward
    rotor.when_rotated_counter_clockwise = reverse
    while True:
        if CounterValue>100:
            CounterValue=100
        if CounterValue<0:
            CounterValue=0
        if NextCounterValue != CounterValue:
            print('Counter = %d' % CounterValue)
            NextCounterValue = CounterValue
        led.value = CounterValue / 100.0     # set dc value as the duty cycle
def destroy():
    button.close()    
    rotor.close()   
    led.close()   
if __name__ == '__main__':     # Program start from here
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
        print("Ending program")