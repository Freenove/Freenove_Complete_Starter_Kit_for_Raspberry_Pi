

#include "Freenove_WS2812_SPI.h"

Freenove_WS2812_SPI::Freenove_WS2812_SPI(uint16_t n, LED_TYPE t)
{
	
	fd = -1;
	mode = 0;
	bits = 8;
	speed = 6250000;

	setLedCount(n);
	setLedType(t);
	setBrightness(255);
	printf("Please note that when using the mosi pins of spi to drive the ledpixel.\n");
	printf("Other spi pins will also be used, please do not use them.\n");
	
	printf("\nSPI0-MOSI: GPIO10(WS2812-PIN)  SPI0-MISO: GPIO9  SPI0-SCLK: GPIO11  SPI0-CE0: GPIO8  SPI0-CE1: GPIO7\n\n");
}
Freenove_WS2812_SPI::~Freenove_WS2812_SPI(void)
{
	closeSPI();
	exit(0);
}

void Freenove_WS2812_SPI::pabort(const char *s)
{
	perror(s);
	abort();
}

void Freenove_WS2812_SPI::writeSPI(unsigned char *array, uint16_t length)
{
	/*
	int ret = -1;
	struct spi_ioc_transfer tr;
	tr.tx_buf = (unsigned long) array;
	tr.rx_buf = (unsigned long) array;
	tr.len = length;
	tr.delay_usecs = 0;
	tr.speed_hz= speed;
	tr.bits_per_word = bits;
	ret = ioctl(fd, SPI_IOC_MESSAGE(1), &tr);
	if(ret < 1)
		pabort("Can't send spi message");
	*/
	int ret = -1;
	ret = write(fd, array, length);
	if(ret < 1)
		pabort("Can't send spi message");
}

void Freenove_WS2812_SPI::closeSPI(void)
{
	if(fd >=0)
	{
		memset(leds,0,sizeof(leds));
		show();
		close(fd);
		fd=-1;
	}
}

void Freenove_WS2812_SPI::Ctrl_C_Handler(int value)
{
	closeSPI();
	exit(0);
}

void Freenove_WS2812_SPI::convertData(unsigned char * colorPt, uint8_t RGBWvalue)
{
	int loop;
	unsigned char _temp;

	for(loop=0;loop < 8;loop+=1)
	{
		_temp = (RGBWvalue & 0x80) ? 0xFC : 0XC0;
		*(colorPt++)=_temp;
		RGBWvalue <<= 1;
	}
}

void Freenove_WS2812_SPI::set_max_priority(void) 
{
	struct sched_param sched;
	memset(&sched, 0, sizeof(sched));
	sched.sched_priority = sched_get_priority_max(SCHED_FIFO);
	sched_setscheduler(0, SCHED_FIFO, &sched);
}

void Freenove_WS2812_SPI::set_default_priority(void) 
{
	struct sched_param sched;
	memset(&sched, 0, sizeof(sched));
	sched.sched_priority = 0;
	sched_setscheduler(0, SCHED_OTHER, &sched);
}

void Freenove_WS2812_SPI::begin(void)
{
	int ret;
	fd = open("/dev/spidev0.0",O_RDWR);
	if(fd <0)
	{
		printf("You can turn on the 'SPI' in 'Interface Options' by using 'sudo raspi-config'.\n");
		pabort("Can't open device\n");
	}

	mode = 0;
	ret = ioctl(fd, SPI_IOC_WR_MODE, &mode);
	if (ret == -1)
		pabort("can't set spi mode");
	/*
	ret = ioctl(fd, SPI_IOC_RD_MODE, &mode);
	if (ret == -1)
		pabort("can't get spi mode");
	*/

	ret = ioctl(fd, SPI_IOC_WR_BITS_PER_WORD, &bits);
	if (ret == -1)
		pabort("can't set bits per word");
	ret = ioctl(fd, SPI_IOC_RD_BITS_PER_WORD, &bits);
	if (ret == -1)
		pabort("can't get bits per word");

	ret = ioctl(fd, SPI_IOC_WR_MAX_SPEED_HZ, &speed);
	if (ret == -1)
		pabort("can't set max speed hz");
	ret = ioctl(fd, SPI_IOC_RD_MAX_SPEED_HZ, &speed);
	if (ret == -1)
		pabort("can't get max speed hz");

	set_max_priority();
}

void Freenove_WS2812_SPI::end(void)
{
	closeSPI();
}

void Freenove_WS2812_SPI::setLedCount(uint16_t n)
{
	ledCounts = n;
	memset(leds,0,ledCounts);
}

uint16_t Freenove_WS2812_SPI::getLedCount(void)
{
	return ledCounts;
}

void Freenove_WS2812_SPI::setLedType(uint8_t t)
{
	led_type = t;
}

void Freenove_WS2812_SPI::setBrightness(uint8_t br)
{
	brightness = br;
}

void Freenove_WS2812_SPI::setLedColorData(int index, uint32_t rgb)
{
	uint8_t r, g, b;
	r = (uint8_t)((rgb>>16) & 0xff);
	g = (uint8_t)((rgb>>8) & 0xff);
	b = (uint8_t)((rgb>>0) & 0xff);
	setLedRGBData(index, r, g, b);
}

void Freenove_WS2812_SPI::setLedRGBData(int index, uint8_t r, uint8_t g, uint8_t b)
{
	leds[index].RGBW.R = (uint8_t)(r * brightness / 255);
	leds[index].RGBW.G = (uint8_t)(g * brightness / 255);
	leds[index].RGBW.B = (uint8_t)(b * brightness / 255);
}

void Freenove_WS2812_SPI::setLedColor(int index, uint32_t rgb)
{
	setLedColorData(index, rgb);
	show();
}

void Freenove_WS2812_SPI::setLedRGB(int index, uint8_t r, uint8_t g, uint8_t b)
{
	setLedRGBData(index, r, g, b);
	show();
}

void Freenove_WS2812_SPI::setAllLedsColorData(uint32_t rgb)
{
	int i;
	for(i = 0; i < ledCounts; i++)
	{
		setLedColorData(i, rgb);
	}
}

void Freenove_WS2812_SPI::setAllLedsRGBData(uint8_t r, uint8_t g, uint8_t b)
{
	int i;
	for(i = 0; i < ledCounts; i++)
	{
		setLedRGBData(i, r, g, b);
	}
}

void Freenove_WS2812_SPI::setAllLedsColor(uint32_t rgb)
{
	setAllLedsColorData(rgb);
	show();
}

void Freenove_WS2812_SPI::setAllLedsRGB(uint8_t r, uint8_t g, uint8_t b)
{
	setAllLedsRGBData(r, g, b);
	show();
}

void Freenove_WS2812_SPI::show(void)
{
	int loop;
	if(fd < 0) return;
	int ResetCount = 320;    //51.2us
	unsigned char *bufferSPI;
	unsigned char *bufferPtr;

	bufferSPI = (unsigned char *)malloc(ResetCount + ledCounts*24);
	memset(bufferSPI,0,(ResetCount + ledCounts*24));
	bufferPtr= &bufferSPI[ResetCount];

	for(loop=0;loop<ledCounts;loop++)
	{
		switch(led_type)
		{
			case TYPE_RGB:
				convertData(bufferPtr, leds[loop].RGBW.R);
				bufferPtr+=8;
				convertData(bufferPtr, leds[loop].RGBW.G);
				bufferPtr+=8;
				convertData(bufferPtr, leds[loop].RGBW.B);
				bufferPtr+=8;
			break;
			case TYPE_RBG:
				convertData(bufferPtr, leds[loop].RGBW.R);
				bufferPtr+=8;
				convertData(bufferPtr, leds[loop].RGBW.B);
				bufferPtr+=8;
				convertData(bufferPtr, leds[loop].RGBW.G);
				bufferPtr+=8;
			break;
			case TYPE_GRB:
				convertData(bufferPtr, leds[loop].RGBW.G);
				bufferPtr+=8;
				convertData(bufferPtr, leds[loop].RGBW.R);
				bufferPtr+=8;
				convertData(bufferPtr, leds[loop].RGBW.B);
				bufferPtr+=8;
			break;
			case TYPE_GBR:
				convertData(bufferPtr, leds[loop].RGBW.G);
				bufferPtr+=8;
				convertData(bufferPtr, leds[loop].RGBW.B);
				bufferPtr+=8;
				convertData(bufferPtr, leds[loop].RGBW.R);
				bufferPtr+=8;
			break;
			case TYPE_BRG:
				convertData(bufferPtr, leds[loop].RGBW.B);
				bufferPtr+=8;
				convertData(bufferPtr, leds[loop].RGBW.R);
				bufferPtr+=8;
				convertData(bufferPtr, leds[loop].RGBW.G);
				bufferPtr+=8;
			break;
			case TYPE_BGR:
				convertData(bufferPtr, leds[loop].RGBW.B);
				bufferPtr+=8;
				convertData(bufferPtr, leds[loop].RGBW.G);
				bufferPtr+=8;
				convertData(bufferPtr, leds[loop].RGBW.R);
				bufferPtr+=8;
			break;
		}
	}
	writeSPI(bufferSPI, ResetCount+ledCounts*24);
	free(bufferSPI);
}

uint32_t Freenove_WS2812_SPI::Wheel(uint8_t pos)
{
	uint32_t WheelPos = pos % 0xff;
	if (WheelPos < 85) 
	{
		return ((255 - WheelPos * 3) << 16) | ((WheelPos * 3) << 8);
	}
	if (WheelPos < 170)
	{
		WheelPos -= 85;
		return (((255 - WheelPos * 3) << 8) | (WheelPos * 3));
	}
	WheelPos -= 170;
	return ((WheelPos * 3) << 16 | (255 - WheelPos * 3));
}

uint32_t Freenove_WS2812_SPI::hsv2rgb(uint32_t h, uint32_t s, uint32_t v)
{
	uint8_t r, g, b;
	h %= 360; // h -> [0,360]
	uint32_t rgb_max = v * 2.55f;
	uint32_t rgb_min = rgb_max * (100 - s) / 100.0f;

	uint32_t i = h / 60;
	uint32_t diff = h % 60;

	// RGB adjustment amount by hue
	uint32_t rgb_adj = (rgb_max - rgb_min) * diff / 60;

	switch (i) 
	{
		case 0:
			r = rgb_max;
			g = rgb_min + rgb_adj;
			b = rgb_min;
		break;
		case 1:
			r = rgb_max - rgb_adj;
			g = rgb_max;
			b = rgb_min;
		break;
		case 2:
			r = rgb_min;
			g = rgb_max;
			b = rgb_min + rgb_adj;
		break;
		case 3:
			r = rgb_min;
			g = rgb_max - rgb_adj;
			b = rgb_max;
		break;
		case 4:
			r = rgb_min + rgb_adj;
			g = rgb_min;
			b = rgb_max;
		break;
		default:
			r = rgb_max;
			g = rgb_min;
			b = rgb_max - rgb_adj;
		break;
	}
	return (uint32_t)(r << 16 | g << 8 | b);
}

