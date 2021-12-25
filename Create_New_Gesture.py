'''
Add a new gesture to database
'''

import random
import csv


#amount of data points from each move we want
dpts = 60

#num is the suggested amount of data points we want
num = 20
#Store the sensor data
gesture = []
data = []
def main():
    num = input("Enter the amount of gesture repetitions(suggested amount is 20):\n")
    num = int(num)
    name = input("What is the English translation of the gesture:\n")
    with open("Gesture_Database/" + str(name) +".csv", 'w', newline='', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        
        for i in range(num):
            data = record()
            # write a row to the csv file
            writer.writerow(data)

#get the time it takes to perform move
def record():
    #get the difference between before and after move is performed for each sensor
    input("Keep all fingers straight, hand perpendicular to the ground, and press Enter to start")
    #Initial flex sensor values for each finger
    thumbF0 = random.randrange(970, 976)
    indexF0 = random.randrange(1020, 1023)
    middleF0 = random.randrange(1020, 1023)
    ringF0 = random.randrange(1020, 1023)
    pinkyF0 = random.randrange(970, 976)
    ax0 = 0
    ay0 = 0
    az0 = 0
    gx0 = 0
    gy0= 0
    gz0 = 0
    input("Press Enter to after move is performed")
    #Post move flex sensor values for each finger
    thumbF1 = random.randrange(980, 1002)
    indexF1 = random.randrange(1010, 1023)
    middleF1 = random.randrange(225, 250)
    ringF1 = random.randrange(215, 245)
    pinkyF1 = random.randrange(1000, 1010)
    ax1 = 0
    ay1 = 0
    az1 = 0
    gx1 = 90
    gy1= 0
    gz1 = 5
    gesture = [thumbF0-thumbF1, indexF0-indexF1, middleF0-middleF1, ringF0-ringF1, pinkyF0-pinkyF1, ax0-ax1, ay0-ay1, az0-az1, gx0-gx1, gy0-gy1, gz1-gz0]
    return gesture

if __name__ == '__main__':
    main()