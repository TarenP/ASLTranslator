'''
Main script that is used for the ASL translations
'''

import pickle
import random
import serial
import numpy as np
from time import sleep
# Import the required module for text 
# to speech conversion
from gtts import gTTS
import os
import pygame

#Serial Addresses
ser1=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser1.baudrate=9600
ser2=serial.Serial("/dev/ttyACM1",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser2.baudrate=9600

with open('model_pickle', 'rb') as f:
    model = pickle.load(f)

dataMatrix =[]
button = 'L'
# #Generate an artificial move to see if the model answers correctly
def main():
    # Language in which you want to convert
    language = 'en'
    pygame.mixer.init()
    while True:
        Button()
        recordedData = Record()
        #initiate text to speech engine
        # The text that you want to convert to audio
        mytext = str(model.predict([recordedData[0]]))
        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed
        myobj = gTTS(text=mytext, lang=language, slow=False)
        # Saving the converted audio in a mp3 file named
        # welcome 
        myobj.save("Final.mp3")
        # Playing the converted file
        pygame.mixer.music.load("Final.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

            

#Return True when button is pressed
def Button():
    global button
    while True:
        #Initial flex sensor values for each finger
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

        #print(parsed1)
        #print(parsed2)

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
                button = parsed1[1]
                print(button)
        if button == 'L':
            while True:
                #get the difference between before and after move is performed for each sensor
                print("Keep all fingers straight, and press button to start")
                #Initial flex sensor values for each finger
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

                #print(parsed1)
                #print(parsed2)

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
                        button = parsed1[1]
                        print(button)
                    if(button == 'H'): # If button has been pressed
                        print("pressed")
                        return

#Record Gesture
def Record():
    while True:
        num = 1
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

        #print(parsed1)
        #print(parsed2)

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
                button = parsed1[1]
            while button =="L":
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

                #print(parsed1)
                #print(parsed2)

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
                        button = parsed1[1]
                    if num ==1:
                        dataMatrix = np.array([finger0, finger1, finger2, finger3, finger4, ax, ay, az, gx, gy])
                    else:
                        data = np.array([finger0, finger1, finger2, finger3, finger4, ax, ay, az, gx, gy])
                        dataMatrix = np.vstack((dataMatrix, data))
                    print(dataMatrix)
                    # write a row to the csv file
                    print("active")
                    if (button == 'H'):
                        temp = []
                        temp.append(getResult(dataMatrix))
                        print(temp)
                        return temp
                    num += 1

def getResult(mat):
    
    # Stores compressed array
    compressedArr = []
    for i in range(len(mat[0])):
        col = []
        for j in range(len(mat)):
            col.append(int(float(mat[j][i])))
        
        append = int(list_average(col))
        print(append)
        compressedArr.append(append)

    return compressedArr
 
def list_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg
# gesture = [thumbF, indexF, middleF, ringF, pinkyF, ax, ay, az, gx, gy, gz]
# test=[]
# test.append(gesture)
# print(model.predict([test[0]]))
if __name__ == '__main__':
    main()