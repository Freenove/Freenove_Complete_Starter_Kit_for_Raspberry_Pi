/**********************************************************************
* Filename    : TouchSensor.c
* Description : Touch Sensor TTP223 Control LED brightness. 
* Author      : www.freenove.com
* modification: 2022/4/20
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <softPwm.h>
#define ledPin    0  	    //define the ledPin
#define SensorPin 1      //define the SensorPin

int SensorState=LOW;    //store the State of button
int lastSensorState=LOW;//store the lastState of Sensor
long lastChangeTime;    //store the change time of Sensor state
long captureTime=10;   //set the stable time for Sensor state 
int Sensorvalue;
int grade=0;

int main(void)
{
    printf("Program is starting...\n");
    wiringPiSetup();              //Initialize wiringPi.	
    softPwmCreate(ledPin, 0, 100);//Creat SoftPWM pin
    pinMode(SensorPin, INPUT);    //Set SensorPin to input
    pullUpDnControl(SensorPin, PUD_DOWN);   //pull up to high level
    while(1){
         Sensorvalue = digitalRead(SensorPin);   //read the current state of Sensor
         if( Sensorvalue != lastSensorState){    //if the Sensor state has changed, record the time point
              lastChangeTime = millis();
        }
        //if changing-state of the Sensor last beyond the time we set, we consider that
         //the current Sensor state is an effective change rather than a buffeting
         if(millis() - lastChangeTime > captureTime){
             //if sensor state is changed, update the data.
              if(Sensorvalue != SensorState){
                  SensorState = Sensorvalue;
                  //if the state is low, it means the action is pressing
                  if(SensorState == HIGH){
                      grade=grade+1;
                      printf("Sensor is pressed!\n");
                  }
              }
         }
         else if(grade==1){
             softPwmWrite(ledPin, 35);
         }
         else if(grade==2){
             softPwmWrite(ledPin, 65);
         }
         else if(grade==3){
             softPwmWrite(ledPin, 100);
         }
         else if(grade==4){
             grade=0;
         }
         else {
             softPwmWrite(ledPin, 0);
         }
         lastSensorState = Sensorvalue;
    }
    return 0;
}
