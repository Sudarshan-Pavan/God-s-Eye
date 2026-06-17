#include <AccelStepper.h>
#include <cvzone.h>
SerialData serialData(2,3);

int ValsRec[2]={320,240};
// Constants for stepper motor and gear specifications
const float stepsPerRevolution = 300;

// Constants for screen resolution
const int screenWidth = 640;
const int screenHeight = 480;
const int Center_X = screenWidth / 2;
const int Center_Y = screenHeight / 2;


const int Y_STEP_PIN = 6;
const int Y_DIR_PIN = 5;
const int X_STEP_PIN = 13;
const int X_DIR_PIN = 12;

AccelStepper stepperX(AccelStepper::DRIVER, X_STEP_PIN, X_DIR_PIN);
AccelStepper stepperY(AccelStepper::DRIVER, Y_STEP_PIN, Y_DIR_PIN);

void setup() {
  
  serialData.begin();
  
  stepperX.setMaxSpeed(1300.0);
  stepperX.setAcceleration(15.0);
  stepperY.setMaxSpeed(1300.0);
  stepperY.setAcceleration(1300.0);
  stepperX.setCurrentPosition(0.0);
  stepperY.setCurrentPosition(0.0);
  // Set the initial positions of the stepper motors (optional
}

void loop() {

  serialData.Get(ValsRec);

  int Detected_Object_X = ValsRec[0];
  int Detected_Object_Y = ValsRec[1];

  // Calculate the errors between detected object's X and Y coordinates and centers
  int errorX = Center_X - Detected_Object_X;
  int errorY = Center_Y - Detected_Object_Y;

  // Determine the direction in which the stepper motor X should rotate
  int directionX;
  directionX = (errorX > 0) ? 1 : -1;

  // Determine the direction in which the stepper motor Y should rotate
  int directionY;
  directionY = (errorY > 0) ? 1 : -1;

  // Calculate the number of degrees to move based on the errors
  float degreesToMoveX = errorX * (360.0 / screenWidth);
  float degreesToMoveY = errorY * (360.0 / screenHeight);

  // Calculate the number of steps to move based on degrees and gear ratio
  float stepsToMoveX = (degreesToMoveX * (stepsPerRevolution / 360.0)) ;
  float stepsToMoveY = (degreesToMoveY * (stepsPerRevolution / 360.0)) ;

  // Rotate the stepper motors to align the object with the center
  stepperX.move(stepsToMoveX * directionX);
  stepperY.move(stepsToMoveY * directionY);

  stepperX.runToPosition();
  stepperY.runToPosition();
  ValsRec[0]=320;
  ValsRec[1]=240;

}