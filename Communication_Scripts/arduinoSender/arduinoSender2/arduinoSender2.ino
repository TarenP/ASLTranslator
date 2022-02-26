void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(2, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(",");
  //Read sensor state
  Serial.print(analogRead(A0));
  Serial.print(",");
  //Read button state
  if (digitalRead(2) == HIGH){
    Serial.print('H');
  }
  else{
    Serial.print('L');
  }
  delay(100);
}
