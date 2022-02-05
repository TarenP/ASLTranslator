#include <Arduino_LSM6DSOX.h>
#include <WiFiNINA.h>

float gx, gy, gz;
float ax, ay, az;

void setup(){

  // Set the baud rate  
  Serial.begin(9600);
  pinMode(18, INPUT);
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
  Serial.println(",");
  Serial.print(analogRead(A0)); Serial.print(",");
  Serial.print(analogRead(A1)); Serial.print(",");
  //Serial.print(analogRead(A2)); Serial.print(",");
  //Serial.print(analogRead(A3)); Serial.print(",");
  //Serial.print(analogRead(A6)); Serial.print(",");
  //Serial.print(ax*10); Serial.print(",");
  //Serial.print(ay*10); Serial.print(",");
  //Serial.print(az*10); Serial.print(",");
  //Serial.print(gx*10); Serial.print(",");
  //Serial.print(gy*10); Serial.print(",");
  //Serial.print(gz*10);
  delay(100);
}
