'''
This script is used for creating a new model from the data already in the database
'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import os,glob
import pickle


#generate an artificial dataset
data = []
target =[]

def main():
    #Go through every gesture's file in the database
    for filename in glob.glob(os.path.join('./Gesture_Database', '*.csv')):
        CSVData = open(filename)
        Array2d_result = np.loadtxt(CSVData, delimiter=",")
        
        #remove the filepath from the name
        name = filename.replace("./Gesture_Database/", "")
        name = name.replace(".csv", "")
        name = ''.join((x for x in name if not x.isdigit()))
        if "True" in name:   
            name = name.replace("True", "")
            temp = getResult(Array2d_result)
            data.append(temp)
            target.append(name)
        else:
            for i in Array2d_result:
                target.append(name)
                i = i.astype(int)
                ls = i.tolist()
                data.append(ls)
        print(data)


    #split data into 20% test and 80% train
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size= 0.25)
    # print(len(x_train))
    # print(len(x_test))
    
    model = LogisticRegression(max_iter = 1e1000000)
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
        for j in range(len(mat)):
            col = np.append(col, mat[j][i])
        append = list_average(col)
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