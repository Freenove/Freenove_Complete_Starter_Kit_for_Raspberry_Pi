
#ifndef _FREENOVE_WS2812_LIB_FOR_RASPBERRY_PI_h
#define _FREENOVE_WS2812_LIB_FOR_RASPBERRY_PI_h

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <signal.h>
#include <stdarg.h>
#include <getopt.h>
#include "clk.h"
#include "gpio.h"
#include "dma.h"
#include "pwm.h"
#include "ws2811.h"

#define RGB                         0x00100800
#define RBG                         0x00100008
#define GRB                         0x00081000
#define GBR                         0x00080010
#define BRG                         0x00001008
#define BGR                         0x00000810

class Freenove_WS2812{
	public:
		ws2811_t ledstring =
							{
								.freq = WS2811_TARGET_FREQ,
								.dmanum = 10,
								.channel =
								{
									[0] =
									{
										.gpionum = 18,
										.invert = 0,
										.count = 8,
										.strip_type = WS2811_STRIP_GRB,
										.brightness = 255,
									},
								},
							};
		Freenove_WS2812(unsigned int gpio_pin = 18,unsigned int led_count = 8,unsigned int  led_type =WS2811_STRIP_GRB);
		int constrain(int value,int min,int max);
		void set_Led_Tpye(unsigned int  led_type =WS2811_STRIP_GRB);
		void set_Led_Brightness(unsigned int brightness = 255);
		void set_Led_Color(unsigned int number,unsigned int r = 0,unsigned int g = 0,unsigned int b = 0);
		void show();
		void clear();
};
#endif




