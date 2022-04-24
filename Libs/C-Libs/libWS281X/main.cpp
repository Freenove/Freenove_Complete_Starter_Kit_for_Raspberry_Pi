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
    /*
    int a=-10;
    a=constrain(a,0,255);
    printf("%d",a);**/
    a= new Freenove_WS2812(18,8,GRB);//pin led_count type
    a->set_Led_Color(0,355,0,0);  
    a->set_Led_Color(5,255,0,0); 
    a->set_Led_Brightness(100);    
    a->show();
    return 0;
    }
