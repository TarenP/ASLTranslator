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
data = np.array([])
target =[]
l = 0 #the spacing that the elements need to be in the array

def main():
    dpts = 10
    #Go through every gesture's file in the database
    for filename in glob.glob(os.path.join('./Gesture_Database', '*.csv')):
        CSVData = open(filename)
        Array2d_result = np.loadtxt(CSVData, delimiter=",")
        print(Array2d_result)
        
        #remove the filepath from the name
        name = filename.replace("./Gesture_Database/", "")
        name = name.replace(".csv", "")
        name = ''.join((x for x in name if not x.isdigit()))
        target.append(name)
        #print(Array2d_result)
        length = len(Array2d_result)
       # print(length)
        l = length/dpts #how many datapoints to extract from the csv file
        l = math.trunc(l)
        #print(l)
        #print(dpts)
        with open(filename, 'w+') as output_file:
            with open(filename) as input_file: #change you file name here
                reader = csv.reader(input_file, delimiter = '\n')
                for i in range(len(Array2d_result)):
                    if i % l != 0:
                        for row in reader:
                            line = row[i]
                            output_file.write(line)
                            output_file.write('\n')
                if len(list(reader)) > 10:
                    for i in range(len(Array2d_result)):
                        if i > 10:
                            for row in reader:
                                line = row[i]
                                output_file.write(line)
                                output_file.write('\n')
        #data.append(Array2d_result)
        print(len(data))
        print(data)


    #split data into 20% test and 80% train
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size= 0.2)
    # print(len(x_train))
    # print(len(x_test))
    
    model = LogisticRegression()
    #train model
    model.fit(x_train, y_train)
    #print the accuracy of model against the test data
    print(model.score(x_test, y_test))
    
    with open('model_pickle', 'wb') as f:
        pickle.dump(model, f)


if __name__ == '__main__':
    main()