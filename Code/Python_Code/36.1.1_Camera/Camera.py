#!/usr/bin/env python3
#############################################################################
# Filename    : Camera.py
# Description : Use the camera to take photos and save them in the appropriate location.  
# Author      : www.freenove.com
# modification: 2022/4/20
########################################################################
import time
import picamera
import RPi.GPIO as GPIO

buttonPin = 11    # define buttonPin
def setup():
    
    GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set buttonPin to PULL UP INPUT mode
def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW: # if button is pressed
            with picamera.PiCamera() as camera:
                my_file = open('image.jpg', 'wb')
                camera.start_preview()
                time.sleep(2)
                camera.capture(my_file)
                print ('Hello.a photo has been to taken successfully')   # print information on terminal
                my_file.close()
def destroy():
    GPIO.cleanup()                    # Release GPIO resource

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    print ('Please preess the button take a photo')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
