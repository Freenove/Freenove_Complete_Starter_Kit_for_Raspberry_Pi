#!/usr/bin/env python3
#############################################################################
# Filename    : Alertor.py
# Description : Make a sound and light reminder with a buzzer and infrared obstacle avoidance sensor.
# Author      : www.freenove.com
# modification: 2023/05/15
########################################################################
from gpiozero import LED, Buzzer
from sensor import InfraredSensor
import time

ledPin    = 27
sensorPin = 18     # define sensorPin
BuzzerPin = 17
sensor = InfraredSensor(sensorPin, pull_up=True)
led    = LED(ledPin, initial_value=False) 
buzzer = Buzzer(BuzzerPin)

def alarm():
    times=3
    while times:
        buzzer.on() # turn on buzzer
        led.on()    # turn on led
        time.sleep(0.05)
        buzzer.off()  # turn off buzzer
        led.off()     # turn on led
        time.sleep(0.05)
        times-=1

# When sensor is blocked, this function will be executed
def SensorEvent(channel): # The sensor is blocked
    alarm()
 
def loop():
    sensor.when_reflect = SensorEvent
    while True:
        time.sleep(1)

def destroy():
    led.close() 
    sensor.close()                     

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        print("Ending program")