#include <Arduino_LSM6DSOX.h>
#include <WiFiNINA.h>

/////////////////////
// IMU Definitions //
/////////////////////
float gx, gy, gz;
float ax, ay, az;

/////////////////////
// Pin Definitions //
/////////////////////
const int selectPins[3] = {4, 5, 6}; // S0~4, S1~5, S2~6
//const int zOutput = 5; 
const int zInput = A0; // Connect common (Z) to A0 (analog input)

void setup(){
   
  // Set the baud rate  
  Serial.begin(9600);
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  // Set up the select pins as outputs:
  for (int i=0; i<3; i++)
  {
    pinMode(selectPins[i], OUTPUT);
    digitalWrite(selectPins[i], HIGH);
  }
  pinMode(zInput, INPUT); // Set up Z as an input
}
 
void loop(){
  Serial.println(",");

  //IMU data
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(ax, ay, az);
  }
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(gx, gy, gz);
  }
  
  // Loop through all 5 pins.
  byte pin = 2;
  selectMuxPin(pin); // Select one at a time
  Serial.print(analogRead(A0)); Serial.print(","); //print sensor data
  pin = 1;
  selectMuxPin(pin); // Select one at a time
  Serial.print(analogRead(A0)); Serial.print(","); //print sensor data
  //Serial.print(ax*10); Serial.print(",");
 // Serial.print(ay*10); Serial.print(",");
 // Serial.print(az*10); Serial.print(",");
 /// Serial.print(gx*10); Serial.print(",");
 // Serial.print(gy*10); Serial.print(",");
//  Serial.print(gz*10);
  delay(100);
}

// The selectMuxPin function sets the S0, S1, and S2 pins
// accordingly, given a pin from 0-4.
void selectMuxPin(byte pin)
{
  for (int i=0; i<3; i++)
  {
    if (pin & (1<<i))
      digitalWrite(selectPins[i], HIGH);
    else
      digitalWrite(selectPins[i], LOW);
  }

}
