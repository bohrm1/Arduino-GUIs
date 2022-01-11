int led = 13;
char pythonInput;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW);

}

void loop() {
  if(Serial.available() > 0) {
    pythonInput = Serial.read();
    if(pythonInput == 'h') {
      digitalWrite(led, HIGH);
    }
    if(pythonInput == 'l') {
      digitalWrite(led, LOW);
    }
  }
delay(5);
}
