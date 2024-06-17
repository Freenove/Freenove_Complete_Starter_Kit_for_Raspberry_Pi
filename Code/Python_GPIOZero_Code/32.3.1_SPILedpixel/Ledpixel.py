#!/usr/bin/env python3
########################################################################
# Filename    : Ledpixel.py
# Description : Use freenve 8RGB LED module to achieve a flowing light.
# Author      : www.freenove.com
# modification: 2024/06/17
########################################################################
from SPI_Ledpixel import Freenove_SPI_LedPixel
import time

# Main program logic follows:
if __name__ == '__main__':     
    # Freenove_SPI_LedPixel(led_count, led_brightness, led_transmission_sequence, spidev_bus)
    led = Freenove_SPI_LedPixel(8, 255, 'GRB', 0)

    try:
        if led.check_spi_state() != 0:
            led.set_led_count(8)                             # Set the number of lights.
            led.set_led_brightness(20)                       # Set the brightness of lights.
            color = [[255,0,0],[0,255,0],[0,0,255],[0,0,0]]  # Set the color of the lights
            for j in range(4):
                for i in range(8):
                    # Set the color of the lights, but it does not take effect
                    led.set_led_rgb_data(i, color[j])        
                    # Send the color data and make the color data effective
                    led.show()
                    time.sleep(0.1)

                    
            while True:
                for j in range(255):
                    for i in range(led.led_count):
                        #Converts values ranging from 0 to 255 to color data.
                        led.set_led_rgb_data(i, led.wheel((round(i * 255 / led.led_count) + j)%256))
                    led.show()
                    time.sleep(0.002)
        else:
            led.led_close()
    except KeyboardInterrupt:
        led.led_close()