const int flexPin = A0;

//Variables:
int value; //save analog value


void setup(){
  Serial.begin(9600);

}

void loop(){
  
  value = analogRead(flexPin);
  Serial.println(value);
  //value = map(value, 700, 900, 0, 255);//Map value 0-1023 to 0-255 (PWM)
  delay(100);                         //Small delay
}
