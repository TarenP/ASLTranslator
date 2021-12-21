import serial # Module needed for serial communication
 
# Set the port name and the baud rate. This baud rate should match the
# baud rate set on the Arduino.
# Timeout parameter makes sure that program doesn't get stuck if data isn't
# being received. After 1 second, the function will return with whatever data
# it has. The readline() function will only wait 1 second for a complete line 
# of input.
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
 
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
  if(len(parsed) > 9):
    print(parsed)
       
    # We add the '0' character to the end of each item in the 
    # parsed list. This makes sure that there are no empty
    # strings in the list. Adding 0 makes sure that we have
    # at least 6 string values we can convert into integers.
    # Dividing by 10 removes the trailing 0 but it makes the integer a float.
    # We then have to convert the float to an integer.
    finger0 = parsed[0]
    finger1 = parsed[1]
    finger2 = parsed[2]
    finger3 = parsed[3]
    finger4 = parsed[4]
    ax = parsed[5]
    ay = parsed[6]
    az = parsed[7]
    gx = parsed[8]
    gy = parsed[9]
    gz = parsed[10]
    