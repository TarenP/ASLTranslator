import serial
import RPi.GPIO as GPIO
import time
 
# Set the port name and the baud rate. This baud rate should match the
# baud rate set on the Arduino.
# Timeout parameter makes sure that program doesn't get stuck if data isn't
# being received. After 1 second, the function will return with whatever data
# it has. The readline() function will only wait 1 second for a complete line 
# of input.
ser1=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser1.baudrate=9600
ser2=serial.Serial("/dev/ttyACM1",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser2.baudrate=9600

finger0 = 0
finger1 = 0
finger2 = 0
finger3 = 0
finger4 = 0
ax = 0
ay = 0
az = 0
gx = 0
gy = 0
gz = 0
button = 0
 
# Infinite loop
while (1):
    line1=ser1.readline().decode()
    line2=ser2.readline().decode()
#     print(line1)
#     print(line2)

    # Take out the commas. Parse the string into a list.
    parsed1 = line1.split(',')
    parsed2 = line2.split(',')

    # rstrip() function removes trailing characters like
    # the new line character '\n' and '/r'. Also removes
    # white space.
    parsed1 = [x.rstrip() for x in parsed1]
    parsed2 = [x.rstrip() for x in parsed2]

    print(parsed1)
    print(parsed2)

    if(len(parsed1)> 9 or len(parsed2)>9):
        # We add the '0' character to the end of each item in the 
        # parsed list. This makes sure that there are no empty
        # strings in the list. Adding 0 makes sure that we have
        # at least 6 string values we can convert into integers.
        # Dividing by 10 removes the trailing 0 but it makes the integer a float.
        # We then have to convert the float to an integer.
        
        #depending on which arduino gets assigned parsed1
        try:
            finger0 = parsed1[0]
            finger1 = parsed1[1]
            finger2 = parsed1[2]
            finger3 = parsed1[3]
            finger4 = parsed2[0]
            ax = parsed1[5]
            ay = parsed1[6]
            az = parsed1[7]
            gx = parsed1[8]
            gy = parsed1[9]
            gz = parsed1[10]
            button = parsed2[1]
        except:
            finger0 = parsed2[0]
            finger1 = parsed2[1]
            finger2 = parsed2[2]
            finger3 = parsed2[3]
            finger4 = parsed1[0]
            ax = parsed2[5]
            ay = parsed2[6]
            az = parsed2[7]
            gx = parsed2[8]
            gy = parsed2[9]
            gz = parsed2[10]
            button = parsed1[1]

