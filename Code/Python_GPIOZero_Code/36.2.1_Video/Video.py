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
from gpiozero import Button
import os

buttonPin = 17    # define buttonPin
button2Pin =18    # define button2Pin
shootbutton = Button(buttonPin,pull_up=True) # define Button pin according to BCM Numbering
openbutton = Button(button2Pin,pull_up=True) # define Button pin according to BCM Numbering

def loop():
    while True:
        if shootbutton.is_pressed:  # if button is pressed
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
                
        elif openbutton.is_pressed:  # if button is pressed
            print ('The video has been opened')  # print information on terminal
            os.system('ffplay -x 640 -y 480 -autoexit  video.h264  -vf setpts=PTS/4 ')  
            print ('The video has been closed')  # print information on terminal
def destroy():
    shootbutton.close()
    openbutton.close()

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    print ('Please preess the button to shoot a video')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        print("Ending program")
