#include <Servo.h>

const int button1Pin = 2;
const int servo1Pin = 9;
const int motor1in1 = 10;
const int motor1in2 = 11;

Servo servo1;

bool button1Pressed = false;

void setup() {
  // Initialize serial communication for debugging
  Serial.begin(9600);
  Serial.println("Initializing setup...");

  servo1.attach(servo1Pin);  // Attach the servo on pin 9 to the servo object
  pinMode(motor1in1, OUTPUT);
  pinMode(motor1in2, OUTPUT);

  // Attach interrupt to the button pin, triggering on RISING edge (button press)
  attachInterrupt(digitalPinToInterrupt(button1Pin), buttonPress, RISING);

  Serial.println("Servo attached, button and motor pins configured.");
}

void loop() {
  // Main loop just handles motor and servo actions when button is pressed
  if (button1Pressed) {
    Serial.println("Button pressed, starting motor and servo action.");

    // Set motor direction and speed
    digitalWrite(motor1in1, LOW);   // Ensure the first motor direction is set to LOW
    analogWrite(motor1in2, 50);     // Set the motor speed

    // Move the servo to 0 degrees
    servo1.write(0);
    Serial.println("Servo moved to 0 degrees.");

    // Delay for a short time to complete action, then stop the motor
    delay(500);
    analogWrite(motor1in2, 0);      // Stop motor speed
    servo1.write(180);              // Reset servo
    Serial.println("Servo moved to 180 degrees.");
    
    // Reset button state
    button1Pressed = false;
  }
}

// Interrupt Service Routine (ISR) for handling button press
void buttonPress() {
  button1Pressed = true;
}
