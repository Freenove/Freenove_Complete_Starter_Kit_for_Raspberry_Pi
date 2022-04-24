/**********************************************************************
* Filename    : Discolor.c
* Description : Touch Sensor TTP223 control RGB LED. 
* Author      : www.freenove.com
* modification: 2022/4/20
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <softPwm.h>
#include <stdlib.h>
#define SensorPin    1	   //define the SensorPin
#define ledPinRed    3
#define ledPinGreen  2
#define ledPinBlue   0

int SensorState=LOW;	//store the State of Sensor
int lastSensorState=LOW;//store the lastState of Sensor
long lastChangeTime;	//store the change time of Sensor state
long captureTime=10;	//set the stable time for Sensor state 
int Sensorvalue;
int grade=0;

void setupLedPin(void)
{
    softPwmCreate(ledPinRed,  0, 100);	//Creat SoftPWM pin for red
    softPwmCreate(ledPinGreen,0, 100);  //Creat SoftPWM pin for green
    softPwmCreate(ledPinBlue, 0, 100);  //Creat SoftPWM pin for blue
}
void setLedColor(int r, int g, int b)
{
    softPwmWrite(ledPinRed,   r);	//Set the duty cycle 
    softPwmWrite(ledPinGreen, g);   //Set the duty cycle 
    softPwmWrite(ledPinBlue,  b);   //Set the duty cycle 
}
int main(void)
{
    int r,g,b;
    printf("Program is starting...\n");
    wiringPiSetup(); //Initialize wiringPi.	
    pinMode(SensorPin, INPUT); //Set SensorPin to input
    pullUpDnControl(SensorPin, PUD_DOWN);  //pull up to high level
    setupLedPin();
    r=100;  
    g=100; 
    b=100; 
    setLedColor(r,g,b); // set  the duty cycle value 
    while(1){
        Sensorvalue = digitalRead(SensorPin); //read the current state of Sensor
        if( Sensorvalue != lastSensorState){  //if the Sensor state has changed, record the time point
            lastChangeTime = millis();
        }
        //if changing-state of the Sensor last beyond the time we set, we consider that 
        //the current Sensor state is an effective change rather than a buffeting
        if(millis() - lastChangeTime > captureTime){
        //if button state is changed, update the data.
            if(Sensorvalue != SensorState){
                  SensorState = Sensorvalue;
                  //if the state is low, it means the action is pressing
                  if(SensorState == HIGH){
                             printf("Sensor is pressed!\n");
                             grade=grade+1;
                  }
            }
        }
        if(grade==1){
            r=0;  
            g=100;  
            b=100;
            setLedColor(r,g,b); //set  the duty cycle value
            printf("r=%d,  g=%d,  b=%d \nThe current color is red\n",r,g,b);	
        }
        else if(grade==2){
            r=100;  
            g=0;  
            b=100;  
            setLedColor(r,g,b); //set  the duty cycle value
            printf("r=%d,  g=%d,  b=%d \nThe current color is green\n",r,g,b);	
        }
        else if(grade==3){
            r=100;  
            g=100;  
            b=0; 
            setLedColor(r,g,b); //set  the duty cycle value
            printf("r=%d,  g=%d,  b=%d \nThe current color is blue\n",r,g,b);	
        }
        else if(grade==4){
            grade=0;
        }
        else {
            r=100;  
            g=100;  
            b=100;  
            setLedColor(r,g,b); //set  the duty cycle value
        }
        lastSensorState = Sensorvalue;
    }
    return 0;
}
