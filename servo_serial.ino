#include <Servo.h>

Servo servo;             //creating servo object 
int serialInput;         //integer to hold serial input

int getAngle() {           //function which converts serial input string to integer
  String signalAngle;
  int intAngle;
  delay(500);
  signalAngle = Serial.readString();        //reading string from serial port
  intAngle = signalAngle.toInt();     //converting string to integer 
  return intAngle;         //returning angle inputed from python script
}
void setup() {
  Serial.begin(9600);
  servo.attach(9);
  // put your setup code here, to run once:

}

void loop() {
  if(Serial.available() > 0) {
    serialInput = getAngle();
    servo.write(serialInput);   //writing angle to servo motor
  }
    delay(100);
}
