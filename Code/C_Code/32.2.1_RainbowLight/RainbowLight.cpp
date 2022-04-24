/**********************************************************************
* Filename    : RainbowLight.cpp
* Description : Use freenve 8RGB LED module to achieve rainbow lights.
* Author      : www.freenove.com
* modification: 2022/4/20
**********************************************************************/
#include <stdio.h>
#include <wiringPi.h>
#include <ADCDevice.hpp>
#include "Freenove_WS2812_Lib_for_Raspberry_Pi.hpp"
Freenove_WS2812 *led;
ADCDevice *adc;  
int red,green,blue;
void HSL_RGB(int degree){
    degree=degree/360.0*255;
    if (degree < 85){
            red = 255 - degree * 3;
            green = degree * 3;
            blue = 0;
    }
    else if (degree < 170){
            degree = degree - 85;
            red = 0;
            green = 255 - degree * 3;
            blue = degree * 3;
    }
    else{
            degree = degree - 170;
            red = degree * 3;
            green = 0;
            blue = 255 - degree * 3;
    }
}
int main(){
    printf("Program is starting ...\n");
    adc = new ADCDevice();
    int i;
    led= new Freenove_WS2812(18,8,GRB);//pin led_count type
    led->set_Led_Brightness(50);
    if(adc->detectI2C(0x4b)){   // Detect the ads7830
        delete adc;               // Free previously pointed memory
        adc = new ADS7830(0x4b);      // If detected, create an instance of ADS7830.
}
    else if(adc->detectI2C(0x48)){    // Detect the pcf8591.
        delete adc;                // Free previously pointed memory
        adc = new PCF8591();    // If detected, create an instance of PCF8591.
    }
    else{
        printf("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        return -1;
    }
    while(1){
        for(i=0;i<8;i++){
            int degree = (int)(adc->analogRead(2)/255.0*360+i*45);    //read analog value of A0 pin
            if (degree > 360){
                degree=degree-360;
            }
            HSL_RGB(degree);
            led->set_Led_Color(i,red,green,blue);  
            led->show();
        }
    }
    return 0;
}
