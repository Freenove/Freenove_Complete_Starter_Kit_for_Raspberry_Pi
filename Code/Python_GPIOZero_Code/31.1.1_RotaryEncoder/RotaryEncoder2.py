#!/usr/bin/env python3
#############################################################################
# Filename    : RotaryEncoder.py
# Description : Use rotary encoder to make a simple counter. 
# Author      : www.freenove.com
# modification: 2023/05/15
########################################################################
from gpiozero import RotaryEncoder,Button
import time
CounterValue = 0
button = Button(27) # define Button pin according to BCM Numbering    
rotor = RotaryEncoder(17, 18,max_steps=30)

def forward():
    global CounterValue
    CounterValue =CounterValue+1
    print('Counter = %d' % CounterValue)

def reverse():
    global CounterValue
    CounterValue =CounterValue-1
    print('Counter = %d' % CounterValue)
def reset():
    global CounterValue
    CounterValue =0
    print('Counter = %d' % CounterValue)

def loop():
    button.when_pressed = reset
    rotor.when_rotated_clockwise = forward
    rotor.when_rotated_counter_clockwise = reverse
    while True:
        pass
def destroy():
    button.close()    
    rotor.close()   
if __name__ == '__main__':     # Program start from here
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
        print("Ending program")