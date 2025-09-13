from gpiozero import LED
from time import sleep

led = LED(17)

def loop():
    while True:
        dot = 0.3
        tire = 1
        pause = 0.2
        br = 5
        
        signals = [dot, dot, dot, tire, tire, tire, dot, dot, dot]
        for signal in signals:
            led.on()
            sleep(signal)
            led.off()
        
            sleep(pause)
    
        sleep(br)
        
    led.close()

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
