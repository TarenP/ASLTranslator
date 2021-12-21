import serial # Module needed for serial communication
 
# Set the port name and the baud rate. This baud rate should match the
# baud rate set on the Arduino.
# Timeout parameter makes sure that program doesn't get stuck if data isn't
# being received. After 1 second, the function will return with whatever data
# it has. The readline() function will only wait 1 second for a complete line 
# of input.
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
 
# Initialize 6 integers
servo_0_angle = 90
servo_1_angle = 90
servo_2_angle = 90
servo_3_angle = 90
servo_4_angle = 90
servo_5_angle = 90
 
# Infinite loop
while (1):
 
  # Read everything until the new line character
  # Convert the data from a byte into a string of type 'utf-8'
  # You could also use 'ascii'
  line = ser.readline().decode('utf-8')
 
  # Take out the commas. Parse the string into a list.
  parsed = line.split(',')
     
  # rstrip() function removes trailing characters like
  # the new line character '\n' and '/r'. Also removes
  # white space.
  parsed = [x.rstrip() for x in parsed]
     
  # We know we need to receive 6 integers. This code helps with any loss
  # of data that might happen as data is transferred between Arduino
  # and the Raspberry Pi.
  if(len(parsed) > 5):
    print(parsed)
       
    # We add the '0' character to the end of each item in the 
    # parsed list. This makes sure that there are no empty
    # strings in the list. Adding 0 makes sure that we have
    # at least 6 string values we can convert into integers.
    # Dividing by 10 removes the trailing 0 but it makes the integer a float.
    # We then have to convert the float to an integer.
    servo_0_angle = int(int(parsed[0]+'0')/10)
    servo_1_angle = int(int(parsed[1]+'0')/10)
    servo_2_angle = int(int(parsed[2]+'0')/10)
    servo_3_angle = int(int(parsed[3]+'0')/10)
    servo_4_angle = int(int(parsed[4]+'0')/10)
    servo_5_angle = int(int(parsed[5]+'0')/10)
  print("Servo 0 Angle: " + str(servo_0_angle))
  print("Servo 1 Angle: " + str(servo_1_angle))
  print("Servo 2 Angle: " + str(servo_2_angle))
  print("Servo 3 Angle: " + str(servo_3_angle))
  print("Servo 4 Angle: " + str(servo_4_angle))
  print("Servo 5 Angle: " + str(servo_5_angle))
     
  # This line proves that we have successfully converted the strings
  # to integers.
  print("Sum of Servos 0 and 1: " + str(servo_0_angle + servo_1_angle))