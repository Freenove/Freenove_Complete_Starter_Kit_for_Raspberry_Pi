/**********************************************************************
* Filename    : Alertor.c
* Description : Make magnetic field detection acousto-optic alarm with buzzer and Hall sensor.   
* Author      : www.freenove.com
* modification: 2022/4/20
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#define ledPin    0  	//define the ledPin
#define sensorPin 1	    //define the buttonPin
#define buzzerPin 2  	//define the buzzerPin

void alarm(int times){
    while(times--){
        digitalWrite(buzzerPin, HIGH);
        digitalWrite(ledPin, HIGH);
        delay(50);
        digitalWrite(buzzerPin, LOW); 
        digitalWrite(ledPin, LOW);
        delay(50);
    }
}

void sensorEven(void){
    alarm(3);
}
void  main(void)
{
    printf("Program is starting ... \n");
    wiringPiSetup();	        //Initialize wiringPi.	
    pinMode(ledPin, OUTPUT);  //Set ledPin to output
    pinMode(sensorPin, INPUT);//Set sensorPin to input
    pinMode(buzzerPin, OUTPUT); 
    delay(100);
    wiringPiISR(sensorPin,INT_EDGE_FALLING,&sensorEven);
    digitalWrite(buzzerPin, LOW); 
    while(1){
    }
}
