/**********************************************************************
* Filename    : InfraredSensor.c
* Description : Infrared Obstacle Avoidance Sensor control LED.
* Author      : www.freenove.com
* modification: 2022/4/20
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#define ledPin    0  	    //define the ledPin
#define sensorPin 1		//define the sensorPin

void  main(void)
{
    printf("Program is starting ... \n");
    wiringPiSetup();	//Initialize wiringPi.	
    pinMode(ledPin, OUTPUT); //Set ledPin to output
    pinMode(sensorPin, INPUT);//Set sensorPin to input
    while(1){
        if(digitalRead(sensorPin) == LOW){ // The sensor is blocked 
            digitalWrite(ledPin, HIGH);  //Make GPIO output HIGH level
            printf("led turned on >>>\n");    //Output information on terminal
        }
        else {							// The sensor is not blocked
            digitalWrite(ledPin, LOW);  //Make GPIO output LOW level
            printf("led turned off <<<\n");//Output information on terminal
        }
    }
}
