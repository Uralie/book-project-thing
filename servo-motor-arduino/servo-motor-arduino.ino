#include <Servo.h>

const int buttonPin = 2;
Servo nine;
const int motor1in1 = 10;
const int motor1in2 = 11;

int buttonState =  0;
//int a = 0;

void setup() {
  // put your setup code here, to run once:

  nine.attach(9);  // attaches the servo on pin 9 to the servo object
  pinMode(buttonPin, INPUT);
  pinMode(motor1in1, OUTPUT);
  pinMode(motor1in2, OUTPUT);
  nine.write(0);

}

void loop() {

/*
  for (a = 0; a < 180; a+=5)
  {
    analogWrite(motor1in2, 50);
    nine.write(a);
    delay(15);
  }
  delay(1000);
  for (a = 180; a > 0; a-=5)
  {
    analogWrite(motor1in2, 0);

    nine.write(a);
    delay(15);
  }
  delay(1000);
}
  */
  // put your main code here, to run repeatedly:
  buttonState = digitalRead(buttonPin);

  digitalWrite(motor1in2, LOW);
  if (buttonState == HIGH) {
    //button1Pressed = true;
    analogWrite(motor1in2, 50);
    delay(1000);
    nine.write(180);
    delay(500);
    nine.write(0);
  }
  
}
