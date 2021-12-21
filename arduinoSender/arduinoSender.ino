int servo_0_angle = 90;
int servo_1_angle = 7;
int servo_2_angle = 63;
int servo_3_angle = 85;
int servo_4_angle = 162;
int servo_5_angle = 45;
 
void setup(){
   
  // Set the baud rate  
  Serial.begin(9600);
   
}
 
void loop(){
   
  Serial.print(servo_0_angle); Serial.print(",");
  Serial.print(servo_1_angle); Serial.print(",");
  Serial.print(servo_2_angle); Serial.print(",");
  Serial.print(servo_3_angle); Serial.print(",");
  Serial.print(servo_4_angle); Serial.print(",");
  Serial.println(servo_5_angle); 
  delay(500);
}
