#define dir_mot1 D6
#define step_mot1 D5
#define dir_mot2 D0
#define step_mot2 D1
#define dir_cd D3
#define step_cd D4
#define enable D2




void setup() {
  pinMode(enPin,OUTPUT);
  digitalWrite(enPin,LOW);
pinMode(dir_mot1,OUTPUT);
pinMode(step_mot1,OUTPUT);
pinMode(dir_mot2,OUTPUT);
pinMode(step_mot2,OUTPUT);
pinMode(dir_cd,OUTPUT);
pinMode(step_cd,OUTPUT);
Serial.begin(9600);
}


void move_cd(int steps){
int interval= 500;
for(int i=0;i<steps;i++){
  
   digitalWrite(step_cd,HIGH);
   delayMicroseconds(interval);
   digitalWrite(step_cd,LOW);
      delayMicroseconds(interval);
}

}
void move_mot1(int steps){
int interval= 1200;
for(int i=0;i<steps;i++){
  
   digitalWrite(step_mot1,HIGH);
   delayMicroseconds(interval);

   digitalWrite(step_mot1,LOW);
}

}
void move_mot2(int steps){
int interval= 1200;
for(int i=0;i<steps;i++){
   digitalWrite(step_mot2,HIGH);
delayMicroseconds(interval);

   digitalWrite(step_mot2,LOW);
}

}



void loop() {
digitalWrite(dir_mot1,HIGH);
digitalWrite(dir_mot2,HIGH);
digitalWrite(dir_cd,HIGH);

move_mot1(200);
move_mot2(200);
move_cd(20);

 digitalWrite(dir_mot1,LOW);
 digitalWrite(dir_mot2,LOW);
 digitalWrite(dir_cd,LOW);

 move_mot1(200);
move_mot2(200);
move_cd(20);


while (true);


}