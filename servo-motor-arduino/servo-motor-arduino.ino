#include <Servo.h>
const int servo1Pin = 9;
const int motor1in1 = 10;
const int motor1in2 = 11;

Servo servo1;

void setup() {
  // put your setup code here, to run once:

  servo1.attach(servo1Pin);  // attaches the servo on pin 9 to the servo object
  servo1.write(180);
  pinMode(motor1in1, OUTPUT);
  pinMode(motor1in2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  //digitalWrite(motor1in1, LOW);
  analogWrite(motor1in2, 200);
  delay(125);
  analogWrite(motor1in2, 0);
  delay(1000);
  for (int i = 180; i > 0; i--){
    servo1.write(i);
    delay(20);
  }
  delay(100);
  servo1.write(180);
  delay(500);
}