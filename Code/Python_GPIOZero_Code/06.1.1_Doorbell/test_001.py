from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)

print("started >>>")
while True:
    buzzer.on()
    sleep(0.5)
    buzzer.off()
    sleep(0.5)

buzzer.close()
print("ended >>>")

