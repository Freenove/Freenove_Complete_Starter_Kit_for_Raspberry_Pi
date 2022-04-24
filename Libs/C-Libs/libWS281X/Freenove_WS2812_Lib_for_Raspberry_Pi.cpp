#include "Freenove_WS2812_Lib_for_Raspberry_Pi.hpp"
Freenove_WS2812::Freenove_WS2812(unsigned int gpio_pin ,unsigned int led_count,unsigned int led_type){
    ledstring.channel[0].gpionum = gpio_pin ;
    ledstring.channel[0].count = led_count ;
    ledstring.channel[0].strip_type = led_type;
    ws2811_init(&ledstring);

}
int Freenove_WS2812::constrain(int value,int min,int max){
    if (value>max){
        return max;
    }
    else if (value<min){
        return min;
    }
    else {
        return value;
    }
}    
void Freenove_WS2812::set_Led_Tpye(unsigned int  type){
    ledstring.channel[0].strip_type = type;
}
    
void Freenove_WS2812::set_Led_Brightness(unsigned int brightness ){
    brightness=constrain(brightness,0,255);
    ledstring.channel[0].brightness = brightness;
}
    
void Freenove_WS2812::set_Led_Color(unsigned int number,unsigned int r,unsigned int g ,unsigned int b ){
    unsigned long color;
    r=constrain(r,0,255);
    g=constrain(g,0,255);
    b=constrain(b,0,255);
    color=(r<<16)|(g<<8)|b;
    ledstring.channel[0].leds[number]=color;
}
    
void Freenove_WS2812::show(){
    ws2811_render(&ledstring);
}
void Freenove_WS2812::clear(){
    for (int i=0;i<ledstring.channel[0].count;i++){
        ledstring.channel[0].leds[i]=0;
    }
    ws2811_render(&ledstring);
    //ws2811_fini(&ledstring);
}

