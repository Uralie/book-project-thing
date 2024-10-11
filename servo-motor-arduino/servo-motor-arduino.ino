#include <Servo.h>

int button1Pin = 2;
Servo nine;
int motor1in1 = 10;
int motor1in2 = 11;


int button1State = 0;
bool button1Pressed = false;
int a = 0;

void setup() {
  // put your setup code here, to run once:

  nine.attach(9);  // attaches the servo on pin 9 to the servo object
  pinMode(button1Pin, INPUT);
  pinMode(motor1in1, OUTPUT);
  pinMode(motor1in2, OUTPUT);
  nine.write(180);
}

void loop() {


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
  /*
  // put your main code here, to run repeatedly:
  button1State = digitalRead(button1Pin);

  digitalWrite(motor1in2, LOW);
  if(button1Pressed){
    //button1Pressed = true;
    nine.write(0);
    analogWrite(motor1in2, 50);
    delay(1000);
    analogWrite(motor1in2, 0);
    nine.write(180);
    delay(500);
    nine.write(0);
    button1Pressed = false;
  }
  
}
void buttonPressed(){
  button1Pressed = true;
}*/
