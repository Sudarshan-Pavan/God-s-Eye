#include <AccelStepper.h>

// Constants for stepper motor and gear specifications
const float stepsPerRevolution = 200; // Steps per revolution of your stepper motor
//const float gearRatio = 1; // Gear ratio of your stepper motor, if applicable

// Constants for screen resolution
const int screenWidth = 640;
const int screenHeight = 480;
const int Center_X = screenWidth / 2;
const int Center_Y = screenHeight / 2;

// Define motor driver pins
const int X_STEP_PIN = 1;
const int X_DIR_PIN = 0;
const int Y_STEP_PIN = 6;
const int Y_DIR_PIN = 5;

// Create the stepper motor objects for X and Y axes
AccelStepper stepperX(AccelStepper::DRIVER, X_STEP_PIN, X_DIR_PIN);
AccelStepper stepperY(AccelStepper::DRIVER, Y_STEP_PIN, Y_DIR_PIN);

void setup() {
  // Setup code for object detection and camera initialization, if applicable
  // ...
  
  // Set the initial positions of the stepper motors (optional)
  stepperX.setCurrentPosition(0);
  stepperY.setCurrentPosition(0);
}

void loop() {
  // Object detection code to get the detected object's X and Y coordinates (Detected_Object_X, Detected_Object_Y)
  // ...
     
  // Calculate the errors between detected object's X and Y coordinates and centers
  int Detected_Object_X = 630;
  int Detected_Object_Y = 470;
  int errorX = Center_X - Detected_Object_X;
  int errorY = Center_Y - Detected_Object_Y;

  // Determine the direction in which the stepper motor X should rotate
  int directionX;

  if (errorX > 0) {
    directionX = 1; // Rotate in the positive direction
  } else {
    directionX = -1; // Rotate in the negative direction
  }

  // Determine the direction in which the stepper motor Y should rotate
  int directionY;

  if (errorY > 0) {
    directionY = 1; // Rotate in the positive direction
  } else {
    directionY = -1; // Rotate in the negative direction
  }

  // Calculate the number of degrees to move based on the errors
  //float degreesToMoveX = errorX * (360.0 / screenWidth);
  //float degreesToMoveY = errorY * (360.0 / screenHeight);

  float degreesToMoveX = errorX / screenWidth;
  float degreesToMoveY = errorY / screenHeight;  

  // Calculate the number of steps to move based on degrees and gear ratio
  //float stepsToMoveX = (degreesToMoveX * (stepsPerRevolution / 360.0));
  //float stepsToMoveY = (degreesToMoveY * (stepsPerRevolution / 360.0));

  float stepsToMoveX = degreesToMoveX * stepsPerRevolution;
  float stepsToMoveY = degreesToMoveY * stepsPerRevolution;

  //float stepsToMoveX = (errorX * stepsPerRevolution)/screenWidth;
  //float stepsToMoveY = (errorY * stepsPerRevolution)/screenHeight;

  // Rotate the stepper motors to align the object with the center
  stepperX.move(stepsToMoveX * directionX);
  stepperY.move(stepsToMoveY * directionY);

  stepperX.setMaxSpeed(200); // Adjust the speed as needed
  stepperY.setMaxSpeed(200); // Adjust the speed as needed

  stepperX.run();
  stepperY.run();

  // Repeat the object detection and motor control loop to track the object
  // ...
}
