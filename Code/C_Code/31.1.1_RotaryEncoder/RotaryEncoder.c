/**********************************************************************
* Filename    : RotaryEncoder.c
* Description : Use rotary encoder to make a simple counter.  
* Author      : www.freenove.com
* modification: 2022/4/20
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>

#define clkPin  0    //define the clkPin
#define dtPin  1     //define the dtPin
#define swPin  2     //define the swPin

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

    while(digitalRead(clkPin) == LOW){      //When not rotating, the value of GPIO.input(clkPin) is 1, and it changes to 0 when rotating
        currentDTStatus = digitalRead(dtPin);  //Record the current value during rotation
        symbol = 1;
    }
    if(symbol==1){                  //When rotating the encoder by hand
        symbol = 0;
        if ((lastDTStatus == 1) && (currentDTStatus == 0)){   //Clockwise rotation, angular displacement increases, count value increases
            previousCounterValue=previousCounterValue+1;
        }
        if ((lastDTStatus == 0) && (currentDTStatus == 1)){   //Counterclockwise rotation, angular displacement decreases, count value decreases
            previousCounterValue=previousCounterValue-1;
        }
    }    
}

void main(void)
{
    printf("Program is starting...\n");
    wiringPiSetup(); //Initialize wiringPi.
    pinMode(clkPin, INPUT); //Set clkPin to input
    pinMode(dtPin, INPUT); //Set dtPin to input
    pinMode(swPin, INPUT); //Set swPin to input
pullUpDnControl(swPin, PUD_UP); //pull up to high level

    while(1){	
        rotaryDeal();
        if(digitalRead(swPin) == LOW){
            delay(120);
            if(digitalRead(swPin) == LOW){   //When the hand presses the rotary encoder, the count value is reset to zero
                previousCounterValue=0;
            }
        }
        if(currentCounterValue != previousCounterValue){
            printf("Counter= %d\n" , previousCounterValue);//
            currentCounterValue = previousCounterValue;
        }
    }
}
