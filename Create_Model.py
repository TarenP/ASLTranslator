'''
This script is used for creating a new model from the data already in the database
'''

from time import sleep
import random
import csv
from numpy import mod
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import os,glob
import pickle
import math


#generate an artificial dataset
data = []
target =[]
l = 0 #the spacing that the elements need to be in the array

def main():
    dpts = 10
    #Go through every gesture's file in the database
    for filename in glob.glob(os.path.join('./Gesture_Database', '*.csv')):
        CSVData = open(filename)
        Array2d_result = np.loadtxt(CSVData, delimiter=",")
        
        #remove the filepath from the name
        name = filename.replace("./Gesture_Database/", "")
        name = name.replace(".csv", "")
        name = ''.join((x for x in name if not x.isdigit()))
        target.append(name)
        Array2d_result = getResult(Array2d_result)
        data.append(Array2d_result)
        print(data)


    #split data into 20% test and 80% train
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size= 0.25)
    # print(len(x_train))
    # print(len(x_test))
    
    model = LogisticRegression(C = 10**5, max_iter = 1e10)
    #train model
    model.fit(x_train, y_train)
    #print the accuracy of model against the test data
    print(model.score(x_test, y_test))
    
    with open('model_pickle', 'wb') as f:
        pickle.dump(model, f)


    # Function to compress
    # matrix to a single number
def getResult(mat):
    
    # Stores compressed array
    compressedArr = []
    for i in range(len(mat[0])):
        col = []
        final_col = []
        for j in range(len(mat)):
            col.append(mat[j][i])
        
        mean = np.mean(col)
        std = np.std(col)
        std_arr = np.bitwise_and(col <= (mean + std), col >= (mean - std))
        for x in range(len(std_arr)):
            if std_arr[x]:
                final_col.append(col[x])
        append = list_average(final_col)
        print(append)
        compressedArr.append(append)

    return compressedArr
 
def list_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

if __name__ == '__main__':
    main()