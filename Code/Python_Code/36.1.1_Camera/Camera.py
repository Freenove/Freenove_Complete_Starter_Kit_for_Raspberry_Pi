#!/usr/bin/env python3
#############################################################################
# Filename    : Camera.py
# Description : Use the camera to take photos and save them in the appropriate location.  
# Author      : www.freenove.com
# modification: 2022/4/20
########################################################################
import time
from picamera2 import Picamera2, Preview
import RPi.GPIO as GPIO

buttonPin = 12    # define buttonPin
def setup():
    
    GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set buttonPin to PULL UP INPUT mode
def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW: # if button is pressed
            picam2 = Picamera2()
            preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
            picam2.configure(preview_config)
            picam2.start_preview(Preview.QTGL)
            picam2.start()
            time.sleep(2)
            metadata = picam2.capture_file("image.jpg")
            print ('Hello.a photo has been to taken successfully')   # print information on terminal
            picam2.close()
            print ('Please preess the button take a photo')
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
