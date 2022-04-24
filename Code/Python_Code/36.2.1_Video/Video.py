#!/usr/bin/env python3
#############################################################################
# Filename    : Video.py
# Description : Use the camera to shoot video and play it.  
# Author      : www.freenove.com
# modification: 2022/4/20
########################################################################
import time
import picamera
import RPi.GPIO as GPIO
import os

buttonPin = 11    # define buttonPin
button2Pin =12    # define button2Pin
def setup():
    GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set buttonPin to PULL UP INPUT mode
    GPIO.setup(button2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set buttonPin to PULL UP INPUT mode

def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW: # if button is pressed
            with picamera.PiCamera() as camera:
                my_file = open('video.h264', 'wb')
                camera.start_preview()
                time.sleep(1)
                camera.resolution=(640,480)
                camera.start_recording(my_file)
                camera.wait_recording(6)
                camera.stop_recording()
                #camera.capture(my_file)
                print ('Hello.a video has been taken successfully')   # print information on terminal
        elif GPIO.input(button2Pin)==GPIO.LOW: # if button is pressed
            print ('The video has been opened')  # print information on terminal
            os.system('ffplay  -autoexit  video.h264')  
            print ('The video has been closed')  # print information on terminal
def destroy():
    GPIO.cleanup()                    # Release GPIO resource

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    print ('Please preess the button to shoot a video')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
