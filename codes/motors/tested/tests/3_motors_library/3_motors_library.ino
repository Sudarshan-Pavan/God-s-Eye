// MultiStepper.pde
// -*- mode: C++ -*-
//
// Shows how to multiple simultaneous steppers
// Runs one stepper forwards and backwards, accelerating and decelerating
// at the limits. Runs other steppers at the same time
//
// Copyright (C) 2009 Mike McCauley
// $Id: MultiStepper.pde,v 1.1 2011/01/05 01:51:01 mikem Exp mikem $
 
#include <AccelStepper.h>
 
// Define some steppers and the pins the will use
AccelStepper stepper1(1, 4, 3); // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
AccelStepper stepper2(1, 6, 5);
AccelStepper stepper3(1, 13, 12);
bool check = 0;
 
void setup()
{  
    stepper1.setMaxSpeed(300.0);
    stepper1.setAcceleration(100.0);
    stepper1.move(265);
    
    stepper2.setMaxSpeed(300.0);
    stepper2.setAcceleration(100.0);
    stepper2.move(200);

    stepper3.setMaxSpeed(300.0);
    stepper3.setAcceleration(100.0);
    stepper3.move(200);
}
 
void loop()
{
    // Change direction at the limits
    if (stepper1.distanceToGo() == 0)
        stepper1.move(-stepper2.currentPosition());
    stepper1.run();
    stepper2.run();
    stepper3.run();
}
