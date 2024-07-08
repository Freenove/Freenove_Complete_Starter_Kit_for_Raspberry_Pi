#ifndef __WS2812_SPI_H
#define __WS2812_SPI_H

#include <stdint.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <fcntl.h>
#include <malloc.h>
#include <string.h>
#include <sys/ioctl.h>
#include <linux/types.h>
#include <linux/spi/spidev.h>
#include <signal.h>
#include <sched.h>
#include <time.h>

#define NbLeds 256

//typedef unsigned char uint8_t;


typedef struct{
  unsigned char B,G,R;
}ledStruct;

union ledUnion {
  unsigned long dw;
  ledStruct RGBW;
};

enum LED_TYPE
{       
    TYPE_RGB = 0,  
    TYPE_RBG = 1,  
    TYPE_GRB = 2,  
    TYPE_GBR = 3,
    TYPE_BRG = 4,  
    TYPE_BGR = 5    
};

class Freenove_WS2812_SPI
{
protected:
	union ledUnion leds[NbLeds];
	int fd;
	uint8_t  mode=0;
	uint8_t  bits=8;
	uint32_t speed=6250000;
	uint8_t ledCounts=8;
	uint8_t rOffset;
	uint8_t gOffset;
	uint8_t bOffset;
	uint8_t led_type=TYPE_GRB;
	uint8_t brightness=255;
	
	void pabort(const char *s);
	void writeSPI(unsigned char *array, uint16_t length);
	void closeSPI(void);
	void Ctrl_C_Handler(int value);
	void convertData(unsigned char *colorPt, uint8_t RGBWvalue);
	void set_max_priority(void);
	void set_default_priority(void);
	
public:
	Freenove_WS2812_SPI(uint16_t n = 8, LED_TYPE t = TYPE_GRB);
	~Freenove_WS2812_SPI(void);
	void begin(void);
	void end(void);
	void setLedCount(uint16_t n);
	uint16_t getLedCount(void);

	void setLedType(uint8_t t);
	void setBrightness(uint8_t br);

	void set_pixel(int index, uint8_t r, uint8_t g, uint8_t b);

	void setLedColorData(int index, uint32_t rgb);
	void setLedRGBData(int index, uint8_t r, uint8_t g, uint8_t b);

	void setLedColor(int index, uint32_t rgb);
	void setLedRGB(int index, uint8_t r, uint8_t g, uint8_t b);

	void setAllLedsColorData(uint32_t rgb);
	void setAllLedsRGBData(uint8_t r, uint8_t g, uint8_t b);

	void setAllLedsColor(uint32_t rgb);
	void setAllLedsRGB(uint8_t r, uint8_t g, uint8_t b);

	void show();

	uint32_t Wheel(uint8_t pos);
	uint32_t hsv2rgb(uint32_t h, uint32_t s, uint32_t v);
	
};


#endif
