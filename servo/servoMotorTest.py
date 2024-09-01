from gpiozero import Motor
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Button
from time import sleep

motor1 = Motor(2, 3)
motor2 = Motor(,) # add pin numbers

button1 = Button(17)
button2 = Button() # add pin number
button1Pressed = False
button2Pressed = False

servo1 = Servo(4,min_pulse_width=0.00075,max_pulse_width=0.00225)
servo1.pin_factory = PiGPIOFactory
servo2 = Servo(,min_pulse_width=0.00075,max_pulse_width=0.00225) # add pin number
servo2.pin_factory = PiGPIOFactory

# print(servo.min_pulse_width)
# print(servo.max_pulse_width)
# print(servo.frame_width)

while True:
    if(button1.is_pressed() and button1Pressed == False){
        button1Pressed = True
        servo1.min()
        motor1.forward(0.2)
        sleep(1)
        motor1.stop()
        servo1.max()
        sleep(0.5)
        servo1.min()
    }
    elif(button1.is_pressed() == False and button1Pressed == True){
        button1Pressed = False
    }

    if(button2.is_pressed() and button2Pressed == False){
        button2Pressed = True
        servo2.min()
        motor2.forward(0.2)
        sleep(1)
        motor2.stop()
        servo2.max()
        sleep(0.5)
        servo2.min()
    }
    elif(button2.is_pressed() == False and button2Pressed == True){
        button2Pressed = False
    }

