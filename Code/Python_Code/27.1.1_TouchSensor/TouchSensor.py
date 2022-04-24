#!/usr/bin/env python3
#############################################################################
# Filename    : TouchSensor.py
# Description : Touch Sensor TTP223 Control LED brightness.
# Author      : www.freenove.com
# modification: 2022/4/20
########################################################################
import RPi.GPIO as GPIO
ledPin = 11       # define ledPin
SensorPin = 12    # define SensorPin
grade=0
def setup():
    global p
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)         # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)     # set ledPin to OUTPUT mode
    GPIO.setup(SensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)     # set SensorPin to PULL UP INPUT mode
    GPIO.output(ledPin,GPIO.LOW)
    p=GPIO.PWM(ledPin,500)
    p.start(0)
def SensorEvent(channel): # When Sensor is pressed, this function will be executed
    global  grade
    grade=grade+1
    print("Sensor is pressed!");
    if(grade==4):
        grade=0;
def loop():
    #Sensor detect 
    GPIO.add_event_detect(SensorPin,GPIO.RISING,callback = SensorEvent,bouncetime=300)
    while True:
        global gears
        if grade==1:
            dc=35
            p.ChangeDutyCycle(dc)
        elif grade==2:
            dc=65
            p.ChangeDutyCycle(dc)
        elif grade==3:
            dc=100
            p.ChangeDutyCycle(dc)
        elif grade==4:
            dc=0
            p.ChangeDutyCycle(dc)
def destroy():
    GPIO.cleanup()                     # Release GPIO resource
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
