#!/usr/bin/env python3
#############################################################################
# Filename    : Video.py
# Description : Use the camera to shoot video and play it.  
# Author      : www.freenove.com
# modification: 2022/4/20
########################################################################
import time
from picamera2.encoders import H264Encoder, Quality
from picamera2 import Picamera2
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
            picam2 = Picamera2()
            video_config = picam2.create_video_configuration(main={"size": (640, 480)})
            picam2.configure(video_config)
            encoder = H264Encoder()
            picam2.start_recording(encoder, 'video.h264', quality=Quality.HIGH)
            print(encoder._bitrate)
            time.sleep(2)
            picam2.stop_recording()
            picam2.close()
            print ('Hello,a video has been taken successfully')   # print information on terminal
                
        elif GPIO.input(button2Pin)==GPIO.LOW: # if button is pressed
            print ('The video has been opened')  # print information on terminal
            os.system('ffplay -x 640 -y 480 -autoexit  video.h264  -vf setpts=PTS/4 ')  
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
