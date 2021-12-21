const int flexPin = A0;

//Variables:
int value; //save analog value
 
void setup(){
   
  // Set the baud rate  
  Serial.begin(9600);
   
}
 
void loop(){
   
  value = analogRead(flexPin);
  Serial.println(value);
  delay(100);
}
