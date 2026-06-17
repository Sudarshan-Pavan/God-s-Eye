#include <AccelStepper.h>
#include <cvzone.h>
SerialData serialData(2,3);

int ValsRec[2]={320,240};
// Constants for stepper motor and gear specifications

// Define the motor interface type (use the one that matches your stepper motor connections)
#define MOTOR_INTERFACE_TYPE 1 // 1: FULL2WIRE, 2: FULL3WIRE, 3: HALF3WIRE, 4: FULL4WIRE, 5: HALF4WIRE

// Constants for screen resolution
const int screenWidth = 640;
const int screenHeight = 480;

const int Center_X = screenWidth / 2; //320.......315-325
const int Center_Y = screenHeight / 2; //240.......235-245

const int right_X = (screenWidth / 2)+5;
const int left_X = (screenWidth / 2)-5;
const int upper_Y = (screenHeight / 2)-5;
const int lower_Y = (screenHeight / 2)+5;

// Define the stepper motor control pins for Motor 1
const int motor1StepPin = 13;
const int motor1DirPin = 12;

// Define the stepper motor control pins for Motor 2
const int motor2StepPin = 6;
const int motor2DirPin = 5;

// Create the stepper motor objects for Motor 1 and Motor 2
AccelStepper motor1(MOTOR_INTERFACE_TYPE, motor1StepPin, motor1DirPin);
AccelStepper motor2(MOTOR_INTERFACE_TYPE, motor2StepPin, motor2DirPin);

const int motor1speed = 1300; // Adjust this value as needed
const int motor2speed = 1300; // Adjust this value as needed

void setup()
{
  serialData.begin();

  // Set the maximum speed and acceleration for both motors
  motor1.setMaxSpeed(motor1speed);
  motor1.setAcceleration(0); // No acceleration
  motor2.setMaxSpeed(motor2speed);
  motor2.setAcceleration(0); // No acceleration

  Serial.begin(9600); // Initialize serial communication (for reading input)
}

void loop() 
{
  serialData.Get(ValsRec);

  int Detected_Object_X = ValsRec[0];
  int Detected_Object_Y = ValsRec[1];
  
  //int Detected_Object_X = 0;
  //int Detected_Object_Y = 0;

  // Calculate the errors between detected object's X and Y coordinates and the region's boundaries
  int errorX = Center_X - Detected_Object_X;
  int errorY = Center_Y - Detected_Object_Y;

  // Determine the direction in which the stepper motor X should rotate
  int directionX;

  if (errorX > 0 && Detected_Object_X < left_X) 
  {
    directionX = -1; // Rotate in the positive direction to move the object to the left
  } 
  else if (errorX < 0 && Detected_Object_X > right_X) 
  {
    directionX = +1; // Rotate in the negative direction to move the object to the right
  } 
  else 
  {
    directionX = 0; // Stop Motor 1
  }

  // Determine the direction in which the stepper motor Y should rotate
  int directionY;

  if (errorY > 0 && Detected_Object_Y < upper_Y) 
  {
    directionY = +1; // Rotate in the positive direction to move the object up
  } 
  else if (errorY < 0 && Detected_Object_Y > lower_Y) 
  {
    directionY = -1; // Rotate in the negative direction to move the object down
  } 
  else 
  {
    directionY = 0; // Stop Motor 2
  }

  // Set the speed and direction for Motor 1
  if (directionX == -1) 
  {
    motor1.setSpeed(motor1speed); // Adjust this value to control the speed for Motor 1 clockwise rotation
  } 
  else if (directionX == 1) 
  {
    motor1.setSpeed(-motor1speed); // Adjust this value to control the speed for Motor 1 anticlockwise rotation
  } 
  else 
  {
    motor1.setSpeed(0); // Stop Motor 1
  }

  // Set the speed and direction for Motor 2
  if (directionY == -1) 
  {
    motor2.setSpeed(motor2speed); // Adjust this value to control the speed for Motor 2 clockwise rotation
  } 
  else if (directionY == 1) 
  {
    motor2.setSpeed(-motor2speed); // Adjust this value to control the speed for Motor 2 anticlockwise rotation
  } 
  else 
  {
    motor2.setSpeed(0); // Stop Motor 2
  }

  // Run both motors continuously
  motor1.run();
  motor2.run();
  
  ValsRec[0]=320;
  ValsRec[1]=240;  
}
