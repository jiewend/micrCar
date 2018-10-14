import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

np.set_
DATA_PATH = '/home/jiewend/workplace/microCar/doc'

def getEachDistFromFile(filePath):
    df = pd.read_csv(filePath, encoding='utf-8', header=None, dtype ={0:str, 1:np.float64, 2:np.float64})
    horizontal = 0
    vertical = 0
    distances = 0
    for i in range(len(df)):
        move = df.iloc[i][1] * df.iloc[i][2]
        if df.iloc[i][0] == 'E':
            horizontal += move
        if df.iloc[i][0] == 'W':
            horizontal -= move

        if df.iloc[i][0] == 'N':
            vertical += move
        if df.iloc[i][0] == 'S':
            vertical -= move
        distances += move
    # print horizontal, vertical, distances
    return round(horizontal, 2), round(vertical, 2), round(distances, 2)

def microcar(expList, actList):
    expHorizontalArr = np.array([])
    expVerticalArr = np.array([])
    expDistancesArr = np.array([])
    actHorizontalArr = np.array([])
    actVerticalArr = np.array([])
    actDistancesArr = np.array([])
    for f in expList:
        h, v, d = getEachDistFromFile(os.path.join(DATA_PATH, f))
        expHorizontalArr = np.append(expHorizontalArr, h)
        expVerticalArr = np.append(expVerticalArr, v)
        expDistancesArr = np.append(expDistancesArr, d)
    for f in actList:
        h, v, d = getEachDistFromFile(os.path.join(DATA_PATH, f))
        actHorizontalArr = np.append(actHorizontalArr, h)
        actVerticalArr = np.append(actVerticalArr, v)
        actDistancesArr = np.append(actDistancesArr, d)
    print  expHorizontalArr, expVerticalArr, actHorizontalArr, actVerticalArr, expDistancesArr, actDistancesArr       
    return [expHorizontalArr, expVerticalArr, actHorizontalArr, actVerticalArr, expDistancesArr, actDistancesArr]
def plotmicrocar(expList, actList):
    data = microcar(expList, actList)
    carCount = len(data[0])

    distPost = np.arange(carCount * 3)
    dist = expDistancesArr

    # fig1 = plt.figure()
    # ax = plt.subplot(111)
    plt.bar(distPost, dist, align='center', alpha=0.5)
    plt.save('a.jpeg')



if __name__ == '__main__':

    # aa = microcar(['exp1.csv', 'exp2.csv'], ['act1.csv', 'act2.csv'])
    plotmicrocar(['exp1.csv', 'exp2.csv'], ['act1.csv', 'act2.csv'])

    

