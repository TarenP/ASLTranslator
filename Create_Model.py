'''
This script is used for creating a new model from the data already in the database
'''

from time import sleep
import random
import csv
import numpy as np
from numpy import mod
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import os,glob
import pickle


#generate an artificial dataset
data = []
gesture = []
target =[]

def main():
    #Go through every gesture's file in the database
    folder_path = '/some/path/to/file'
    for filename in glob.glob(os.path.join('./Gesture_Database', '*.csv')):
        with open(filename, 'r') as f:
            f = open(filename, encoding='UTF8')
            csv_reader = csv.reader(f)
            x = list(csv_reader)
            result = np.array(x).astype("float")
            print(result)
            # data.append(gesture)
            # #remove the filepath from the name
            # name = filename.replace("./Gesture_Database\\", "")
            # name = name.replace(".csv", "")
            # target.append(name)

    # #split data into 20% test and 80% train
    # x_train, x_test, y_train, y_test = train_test_split(data, target, test_size= 0.2)
    # # print(len(x_train))
    # # print(len(x_test))
    
    # model = LogisticRegression()
    # #train model
    # model.fit(x_train, y_train)
    # #print the accuracy of model against the test data
    # print(model.score(x_test, y_test))
    
    # with open('model_pickle', 'wb') as f:
    #     pickle.dump(model, f)

if __name__ == '__main__':
    main()