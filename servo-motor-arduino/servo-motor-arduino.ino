void loop() {
  // put your main code here, to run repeatedly:
  button1State = digitalRead(button1Pin);

  digitalWrite(motor1in1, LOW)
  if(button1State == HIGH && !button1Pressed){
    button1Pressed = true;
    servo1.write(0);
    analogWrite(motor1in2, 50);
    delay(1000);
    analogWrite(motor1in2, 0);
    servo1.write(180);
    delay(500);
    servo1.write(0);
  }
  else if(button1State == LOW && button1Pressed){ //debounce
    button1Pressed = false;
  }
}

}

// Interrupt Service Routine (ISR) for handling button press
void buttonPress() {
  button1Pressed = true;
}
