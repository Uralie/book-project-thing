from gpiozero import Motor
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Button
from time import sleep

motor = Motor(2, 3)
button = Button(17)

servo = Servo(4,min_pulse_width=0.00075,max_pulse_width=0.00225)
servo.pin_factory = PiGPIOFactory
print(servo.min_pulse_width)
print(servo.max_pulse_width)
print(servo.frame_width)

while True:
    button.wait_for_press()
    servo.min()
    motor.forward(0.2)
    sleep(1)
    motor.stop()
    servo.max()
    sleep(0.5)
    servo.min()
