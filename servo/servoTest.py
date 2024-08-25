from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

servo = Servo(2,min_pulse_width=0.00075,max_pulse_width=0.00225)
servo.pin_factory = PiGPIOFactory
print(servo.min_pulse_width)
print(servo.max_pulse_width)
print(servo.frame_width)

while True:
    servo.max()
    sleep(0.5)
    servo.min()
    sleep(0.5)