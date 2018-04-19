int led0 = 13;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led0, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  char read = Serial.read();
  if(read == '2') {
    digitalWrite(led0, 1);
  }
  else if(read == '3') {
    digitalWrite(led0, 0);
  }
}
