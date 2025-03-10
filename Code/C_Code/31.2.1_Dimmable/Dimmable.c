/**********************************************************************
* Filename    : Dimmable.c
* Description : Use rotary encoder to control LED brightness.  
* Author      : www.freenove.com
* modification: 2022/4/20
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#include <softPwm.h>

#define clkPin  0    // define the clkPin
#define dtPin   1    // define the dtPin
#define swPin   2    // define the swPin
#define ledPin  3    //define the ledPin

int symbol = 0;
int lastDTStatus = 0;
int currentDTStatus = 0;
int previousCounterValue= 0;
int currentCounterValue=0;

void rotaryDeal(){
    int symbol= 0;
    int lastDTStatus= 0;
    int currentDTStatus= 0;
    lastDTStatus =digitalRead(dtPin);

    while(digitalRead(clkPin) == LOW){    // When not rotated, the value of GPIO.input(CLKPin) is 1, and it will change to 0 when rotated.
        currentDTStatus = digitalRead(dtPin);  // Record the current value during rotation.
        symbol = 1;
    }
    if(symbol==1){                  // When rotating the encoder by hand.
        symbol = 0;
        if((lastDTStatus == 1) && (currentDTStatus == 0)){     // Clockwise rotation increases angular displacement and count value.
            previousCounterValue=previousCounterValue+1;
        }
        if ((lastDTStatus == 0) && (currentDTStatus == 1)){    // Counterclockwise rotation decreases angular displacement and count value.
            previousCounterValue=previousCounterValue-1;
        }
    }   
}

void main(void){
    printf("Program is starting...\n");
    wiringPiSetup();        //Initialize wiringPi.
    pinMode(clkPin, INPUT); //Set buttonPin to input
    pinMode(dtPin, INPUT);  //Set buttonPin to input
    pinMode(swPin, INPUT);  //Set buttonPin to input
    pullUpDnControl(swPin, PUD_UP); //pull up to high level
    softPwmCreate(ledPin,0,100);
    
    while(1){	
        rotaryDeal();		
        if(digitalRead(swPin) == LOW){
            delay(120);
            if(digitalRead(swPin) == LOW){   // When the rotary encoder is pressed by hand, the count value is reset to zero.
                previousCounterValue=0;
            }
        }
        if(previousCounterValue>=100){
            previousCounterValue=100;
        }
        if(previousCounterValue<=0){
            previousCounterValue=0; 
        }
        if(currentCounterValue != previousCounterValue){
            printf("Counter= %d\n" , previousCounterValue);//
            currentCounterValue = previousCounterValue;
        }
        softPwmWrite(ledPin,previousCounterValue);    //Mapping to PWM duty cycle
    }
}
