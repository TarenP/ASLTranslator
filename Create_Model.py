'''
This script is used for creating a new model from the data already in the database
'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import os,glob
import pickle
import pandas as pd


#generate an artificial dataset
data = []
target =[]
dfs = {}
stat_df = {}
#label columns
root_dir ="/home/pi/Desktop/ASLTranslator/Gesture_Database"
columns = ["finger0", "finger1", "finger2", "finger3", "finger4", "ax", "ay", "az", "gx", "gy"]

def main():
    i = 0
    #Go through every gesture's file in the database
    for f in os.listdir(root_dir):
        name = f.replace(".csv", "")
        name = ''.join((x for x in name if not x.isdigit()))
        direc = os.path.join(root_dir,f)
        dfs[f.split(".")[0]] = pd.read_csv(direc,names=columns)
        dfs[f.split(".")[0]]['Label'] = np.array([name]*len(dfs[f.split(".")[0]]))
        if i == 0:
            first = name
        elif i == 1:
            stat_df = dfs[first].append(dfs[name])
        else:
            stat_df = stat_df.append(dfs[name])
        print(stat_df)
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
    moving = False #tell if the gesture has a time axis or not
    for i in range(len(mat[0])):
        col = []
        for j in range(len(mat)):
            col = np.append(col, mat[j][i])
        #print(np.percentile(col,90) - np.percentile(col,10))
        if i >= 5 and i <= 7: #accelerometer data
            if np.percentile(col,90) - np.percentile(col,10) >= 4:
                moving = True
        if i >= 8: #gyro data
            if np.percentile(col,90) - np.percentile(col,10) >= 200:
                moving = True
        if i <= 4: #Fingers data
            if np.percentile(col,90) - np.percentile(col,10) >= 300:
                moving = True
            
    for i in range(len(mat[0])):
        col = []
        for j in range(len(mat)):
            col = np.append(col, mat[j][i])
        if moving:
            pass #don't filter data
        else:
            mean = np.mean(col)
            std = np.std(col)
            std_arr = np.bitwise_and(col <= (mean + std), col >= (mean - std))
            col[std_arr]
        
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