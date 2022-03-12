'''
This script is used for creating a new model from the data already in the database
'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
import os,glob
import pickle


#generate an artificial dataset
dataPI = []
dataR = []
dataM = []
dataPO = []
dataT = []
dataAX = []
dataAY = []
dataAZ = []
dataGX = []
dataGY = []
target =[]

datasets = ['dataPI', 'dataR', 'dataM', 'dataPO', 'dataT', 'dataAX', 'dataAY', 'dataAZ', 'dataGX', 'dataGY']
def main():
    #Go through every gesture's file in the database
    for filename in glob.glob(os.path.join('./Gesture_Database', '*.csv')):
        CSVData = open(filename)
        Array2d_result = np.loadtxt(CSVData, delimiter=",")
        
        #remove the filepath from the name
        name = filename.replace("./Gesture_Database/", "")
        name = name.replace(".csv", "")
        name = ''.join((x for x in name if not x.isdigit()))
        for i in Array2d_result:
            target.append(name)
            i = i.astype(int)
            ls = i.tolist()
            dataPI.append(ls[0])
            dataR.append(ls[1])
            dataM.append(ls[2])
            dataPO.append(ls[3])
            dataT.append(ls[4])
            dataAX.append(ls[5])
            dataAY.append(ls[6])
            dataAZ.append(ls[7])
            dataGX.append(ls[8])
            dataGY.append(ls[9])

    for i in datasets:
        #split data into 25% test and 80% train
        x_train, x_test, y_train, y_test = train_test_split(i, target, test_size= 0.25)
        # print(len(x_train))
        # print(len(x_test))
        
        #model = LogisticRegression(max_iter = 1e1000000)
        model = GaussianNB()
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