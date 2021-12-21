#include <Arduino_LSM6DSOX.h>
const int flexPin = A0;


//Variables:
int value; //save analog value
float gx, gy, gz;
float ax, ay, az;
 
void setup(){
   
  // Set the baud rate  
  Serial.begin(9600);
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
}
 
void loop(){
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(ax, ay, az);
  }
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(gx, gy, gz);
  }
  Serial.println(analogRead(flexPin));
  Serial.print(analogRead(flexPin)); Serial.print(",");
  Serial.print(analogRead(flexPin)); Serial.print(",");
  Serial.print(analogRead(flexPin)); Serial.print(",");
  Serial.print(analogRead(flexPin)); Serial.print(",");
  Serial.print(ax); Serial.print(",");
  Serial.print(ay); Serial.print(",");
  Serial.print(az); Serial.print(",");
  Serial.print(gx); Serial.print(",");
  Serial.print(gy); Serial.print(",");
  Serial.print(gz);
  delay(100);
}
