/**********************************************************************
* Filename    : Ledpixel.cpp
* Description : Use freenve 8RGB LED module to achieve a flowing light.
* Author      : www.freenove.com
* modification: 2022/4/20
**********************************************************************/
#include <wiringPi.h>
#include "Freenove_WS2812_Lib_for_Raspberry_Pi.hpp"
Freenove_WS2812 *a;
int constrain(int value,int min,int max){
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
int main(){
    printf("Program is starting ...\n");
    while(1){
    int i;
    a= new Freenove_WS2812(18,8,GRB);//pin led_count type
    a->set_Led_Brightness(50); 
    for(i=0;i<8;i++){
        a->set_Led_Color(i,255,0,0);  
        a->show();
        delay(100);
    }
    for(i=0;i<8;i++){
        a->set_Led_Color(i,0,255,0);  
        a->show();
        delay(100);
    }
    for(i=0;i<8;i++){
        a->set_Led_Color(i,0,0,255);  
        a->show();
        delay(100);
    }
    a->clear();
    }
    return 0;
}
