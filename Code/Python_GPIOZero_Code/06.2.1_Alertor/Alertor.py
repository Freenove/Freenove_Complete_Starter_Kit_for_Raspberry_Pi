#!/usr/bin/env python3
########################################################################
# Filename    : Alertor.py
# Description : Make Alertor with buzzer and button
# Author      : www.freenove.com
# modification: 2019/12/27
########################################################################
from gpiozero import TonalBuzzer,Button
from gpiozero.tones import Tone
import time
import math

buzzer = TonalBuzzer(17)
button = Button(18) # define Button pin according to BCM Numbering

def loop():
    while True:
        if button.is_pressed:  # if button is pressed
            alertor()
            # print ('alertor turned on >>> ')
        else :
            stopAlertor()
            # print ('alertor turned off <<<')
def alertor():
    for x in range (0, 361):
        sinVal = math.sin(x * (math.pi / 180.0))
        
        # TonalBuzzer: min_tone.frequency == 220
        # TonalBuzzer: max_tone.frequency == 880
        # sin [-1..1]
        # middle = (880 - 220) / 2 +220 = 550
        # sin [-1..1] -> sin * 330 = [-330..330]
        # [-330..330] + 550 = [220..880] from min to max frequency
        toneVal = 550 + sinVal * 330

        buzzer.play(Tone(toneVal))
        time.sleep(0.005)
        
def stopAlertor():
    buzzer.stop()
            
def destroy():
    buzzer.close()                  

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        print("Ending program")