#include <Servo.h>

#define buttonP1in = 2
#define servo1Pin = 9
#define motor1in1 = 10
#define motor1in2 = 11

void setup() {
  // put your setup code here, to run once:
  Servo servo1;

  servo1.attach(servo1Pin);  // attaches the servo on pin 9 to the servo object
  pinMode(button1Pin, INPUT);
  pinMode(motor1in1, OUTPUT);
  pinMode(motor1in2, OUTPUT);

  bool button1Pressed = false;
}

void loop() {
  // put your main code here, to run repeatedly:
  button1State = digitalRead(button1Pin);

  if(button1State == HIGH && !button1Pressed){
    button1Pressed = true
    servo1.write(0);
    analogWrite(motor1in2, 50);
    delay(1000);
    analogWrite(motor1in2, 0);
    servo1.write(180);
    delay(500);
    servo1.write(0);
  }
  else if(button1State == LOW && button1Pressed){ //debounce
    button1Pressed = false
  }
}
