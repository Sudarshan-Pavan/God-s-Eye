const int dirPin = 3;
const int dirPin1 = 5;
const int dirPin2 = 12;
const int stepPin = 4;
const int stepPin1 = 6;
const int stepPin2 = 13;
const int enable = 2;
//const int stepsPerRevolution = 265;
bool check = 0;

void setup()
{
  // Declare pins as Outputs
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(dirPin2, OUTPUT);
  pinMode(stepPin2, OUTPUT);
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);
  pinMode(enable, OUTPUT);
  digitalWrite(enable, LOW);
}

void move(int step,int dir,int steps)
{
  for(int x = 0; x < steps; x++)
  {
    digitalWrite(step, HIGH);
    delayMicroseconds(4000);
    digitalWrite(step, LOW);
    delayMicroseconds(4000);
    /*if(x==steps)
    break;*/
  }  
}

void loop()
{
  
  check=(check==0)?1:0;
  digitalWrite(3, check);
  digitalWrite(5, check);
  digitalWrite(12, check);s
  move(13, 12, 200);
  move(6, 5, 200);  
  move(4, 3, 265);
}