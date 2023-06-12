#!/usr/bin/env python3
#############################################################################
# Filename    : Camera.py
# Description : Use the camera to take photos and save them in the appropriate location.  
# Author      : www.freenove.com
# modification: 2023/05/11
########################################################################
import time
from picamera2 import Picamera2, Preview
from gpiozero import Button

buttonPin = 18    # define buttonPin
button = Button(buttonPin,pull_up=True) # define Button pin according to BCM Numbering

def loop():
    while True:
        if button.is_pressed:  # if button is pressed
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
    button.close()
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    print ('Please preess the button take a photo')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        print("Ending program")
