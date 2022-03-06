'''
This script is used for creating a new model from the data already in the database
'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import os,glob
import pickle
import csv


#generate an artificial dataset
data = []
target =[]

def main():
    #Go through every gesture's file in the database
    for filename in glob.glob(os.path.join('./Gesture_Database', '*.csv')):
        #remove the filepath from the name
        name = filename.replace("./Gesture_Database/", "")
        name = name.replace(".csv", "")
        name = ''.join((x for x in name if not x.isdigit()))
        with open(filename, "r") as f:
            CSVData = csv.reader(f)
            for i, line in enumerate(CSVData):
                target.append(name)
                data.append(line)
        #print(data)


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


if __name__ == '__main__':
    main()