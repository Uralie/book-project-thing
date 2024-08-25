from gpiozero import Motor
from time import sleep

motor = Motor(2, 3)

while True:
    motor.forward()
    sleep(1)
    motor.backward()
    sleep(1)
