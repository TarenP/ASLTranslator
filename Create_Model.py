'''
This script is used for creating a new model from the data already in the database
'''

from time import sleep
import random
from numpy import mod
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#Flex sensor values for each finger
thumbF = 0
indexF = 0
middleF = 0
ringF = 0
pinkyF = 0
ax = 0
ay = 0
az = 0
gx = 0
gy= 0
gz = 0

#generate an artificial dataset
data = []
gesture = []
target =[]

#x is the amount of data points we want for the number 1 in sign language
x = 10
#y is the amount of data points we wantfor the number 2 in sign language
y = 10

def main():
    #generate ASL 1 data
    for i in range(x):
        thumbF = random.randrange(980, 1002)
        indexF = random.randrange(1005, 1023)
        middleF = random.randrange(225, 250)
        ringF = random.randrange(215, 245)
        pinkyF = random.randrange(970, 1010)
        ax = 0
        ay = 0
        az = 0
        gx = 90
        gy= 0
        gz = 5
        gesture = [thumbF, indexF, middleF, ringF, pinkyF, ax, ay, az, gx, gy, gz]
        data.append(gesture)
        target.append("1")
    #generate ASL 2 data
    for i in range(y):
        thumbF = random.randrange(980, 1002)
        indexF = random.randrange(1018, 1023)
        middleF = random.randrange(1016, 1021)
        ringF = random.randrange(215, 245)
        pinkyF = random.randrange(975, 1010)
        ax = 0
        ay = 0
        az = 0
        gx = 90
        gy= 0
        gz = 5
        gesture = [thumbF, indexF, middleF, ringF, pinkyF, ax, ay, az, gx, gy, gz]
        data.append(gesture)
        target.append("2")
    
    #split data into 20% test and 80% train
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size= 0.2)
    print(len(x_train))
    print(len(x_test))
    
    model = LogisticRegression()
    #train model
    model.fit(x_train, y_train)
    #print the accuracy of model against the test data
    print(model.score(x_test, y_test))
    
    #Generate an artificial move to see if the model answers correctly
    thumbF = 1003
    indexF = 1004
    middleF = random.randrange(225, 250)
    ringF = random.randrange(215, 245)
    pinkyF = random.randrange(970, 1010)
    ax = 0
    ay = 0
    az = 0
    gx = 0
    gy= 0
    gz = 5
    gesture = [thumbF, indexF, middleF, ringF, pinkyF, ax, ay, az, gx, gy, gz]
    test=[]
    test.append(gesture)
    print(model.predict([test[0]]))

if __name__ == '__main__':
    main()