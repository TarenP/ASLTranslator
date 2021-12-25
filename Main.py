'''
Main script that is used for the ASL translations
'''

import pickle
import random

with open('model_pickle', 'rb') as f:
    model = pickle.load(f)

# #Generate an artificial move to see if the model answers correctly
# thumbF = 1003
# indexF = 50
# middleF = random.randrange(225, 250)
# ringF = random.randrange(215, 245)
# pinkyF = random.randrange(970, 1010)
# ax = 0
# ay = 0
# az = 0
# gx = 0
# gy= 0
# gz = 5
# gesture = [thumbF, indexF, middleF, ringF, pinkyF, ax, ay, az, gx, gy, gz]
# test=[]
# test.append(gesture)
# print(model.predict([test[0]]))