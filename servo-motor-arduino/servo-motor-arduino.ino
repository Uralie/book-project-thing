#include <Servo.h>

const int button1Pin = 2;
const int servo1Pin = 9;
const int motor1in1 = 10;
const int motor1in2 = 11;

Servo servo1;

int button1State = 0;
bool button1Pressed = false;

void setup() {
  // put your setup code here, to run once:

  servo1.attach(servo1Pin);  // attaches the servo on pin 9 to the servo object
  servo1.write(180);
  pinMode(button1Pin, INPUT);
  pinMode(motor1in1, OUTPUT);
  pinMode(motor1in2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  button1State = digitalRead(button1Pin);

  digitalWrite(motor1in1, LOW);
  if(button1State == HIGH && button1Pressed==false){
    button1Pressed = true;
    servo1.write(0);
    analogWrite(motor1in2, 70);
    delay(1000);
    analogWrite(motor1in2, 0);
    servo1.write(180);
    delay(500);
    servo1.write(0);
  }
  else if(button1State == LOW && button1Pressed==true){ //debounce
    button1Pressed = false;
  }
}