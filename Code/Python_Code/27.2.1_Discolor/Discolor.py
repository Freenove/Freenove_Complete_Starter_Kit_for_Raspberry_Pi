#!/usr/bin/env python3
#############################################################################
# Filename    : Discolor.py
# Description : Touch Sensor TTP223 control RGB LED.
# Author      : www.freenove.com
# modification: 2022/4/20
########################################################################
import RPi.GPIO as GPIO

SensorPin = 12    # define SensorPin
pins = [15, 13, 11]         # define the pins for R:15,G:13,B:11
grade=0

def setup():
    global pwmRed,pwmGreen,pwmBlue
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)         # use PHYSICAL GPIO Numbering
    GPIO.setup(SensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)     # set SensorPin to PULL DOWN INPUT mode
    GPIO.setup(pins, GPIO.OUT)     # set RGBLED pins to OUTPUT mode
    GPIO.output(pins, GPIO.HIGH)   # make RGBLED pins output HIGH level
    pwmRed = GPIO.PWM(pins[0], 2000)      # set PWM Frequence to 2kHz
    pwmGreen = GPIO.PWM(pins[1], 2000)  # set PWM Frequence to 2kHz
    pwmBlue = GPIO.PWM(pins[2], 2000)    # set PWM Frequence to 2kHz
    pwmRed.start(0)      # set initial Duty Cycle to 0
    pwmGreen.start(0)
    pwmBlue.start(0)
    
def SensorEvent(channel): # When Sensor is pressed, this function will be executed
    global  grade
    grade=grade+1
    print("Sensor is pressed!\n")

def setColor(r_val,g_val,b_val):      # change duty cycle for three pins to r_val,g_val,b_val
    pwmRed.ChangeDutyCycle(r_val)     # change pwmRed duty cycle to r_val
    pwmGreen.ChangeDutyCycle(g_val)   
    pwmBlue.ChangeDutyCycle(b_val)
   
def loop():
    GPIO.add_event_detect(SensorPin,GPIO.RISING,callback = SensorEvent,bouncetime=300)
    while True:
        global grade
        if grade==1:
            r=0  
            g=100
            b=100
            setColor(r,g,b)          #set a duty cycle value 
            print ('r=%d, g=%d, b=%d ' %(r ,g, b))
            print ('The current color is red')
        elif grade==2:
            r=100  
            g=0
            b=100
            setColor(r,g,b)          #set a duty cycle value 
            print ('r=%d, g=%d, b=%d ' %(r ,g, b))
            print ('The current color is green')
        elif grade==3:
            r=100  
            g=100
            b=0
            setColor(r,g,b)          #set a duty cycle value 
            print ('r=%d, g=%d, b=%d ' %(r ,g, b))
            print ('The current color is blue')
        elif grade==4:
            grade=0
        else:
            r=100  
            g=100
            b=100
            setColor(r,g,b)          #set a duty cycle value 
            print ('r=%d, g=%d, b=%d ' %(r ,g, b))
def destroy():
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    GPIO.cleanup()                     # Release GPIO resource
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
