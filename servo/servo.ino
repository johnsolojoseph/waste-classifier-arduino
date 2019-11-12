#include<Servo.h>

Servo servo; 
#define servoPin 9
int flag;

void left() {
  servo.write(125);
  delay(2000);
  servo.write(155);
  delay(2000);
}

void right() {
  servo.write(360);
  delay(5000);
  servo.write(155);

}


void setup() {
  // put your setup code here, to run once:

  servo.attach(servoPin);
  servo.write(155);

  Serial.begin(9600);
}

void loop() {
  // Execute only if data is available from serial
    if (Serial.available() > 0) {
      delay(100);
      flag = Serial.read();
      Serial.print(flag);

      //
      if(flag == '0'){
        left();
      } else if (flag == '1'){
        right();      
      }
    }

 
  

}
