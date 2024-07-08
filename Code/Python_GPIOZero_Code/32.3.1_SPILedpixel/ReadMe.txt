Before you start learning the code, do a few things:
1, Open the terminal. 

2, Enter the command: sudo raspi-config

3, Select Interface Options, then SPI, and turn it on.

4, Enter the command：sudo nano /boot/firmware/config.txt

5, If your Raspberry PI is 4 or 5, add a line at the bottom: force_turbo=1
   If your Raspberry PI is 3, add a line at the bottom: core_freq=250
   
6, Reboot the Raspberry PI.
	   
Then, you can look up spidev0.0 with instructions: ls /dev/spidev*
You can also query the current CPU frequency: vcgencmd measure_clock core
