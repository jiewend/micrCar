import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

LIB_PATh = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(LIB_PATh, '../doc')

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
    print horizontal, vertical, distances
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
    return [expHorizontalArr, expVerticalArr, actHorizontalArr, actVerticalArr, expDistancesArr, actDistancesArr]

def plotmicrocar(expList, actList):
    data = microcar(expList, actList)
    carCount = len(data[0])
    distPost = np.arange(carCount) - 0.15
    fig1 = plt.figure(1)
    plt.bar(distPost, data[-2], alpha=0.5, width=0.3, color='blue', label='Exp')
    plt.bar(distPost + 0.3, data[-1], alpha=1, width=0.3, color='black', label='Actual')
    plt.title('Distance')
    plt.legend()
    fig1.savefig('../doc/Distance.jpeg')

    fig2 = plt.figure(2)
    forplot = np.array([data[0], data[1]])
    for i in range(carCount):
        plt.scatter(forplot[0, i], forplot[1, i], label='mivCar'+str(i))
    plt.xlim(-60, 60)
    plt.ylim(-60, 60)
    plt.legend(loc='upper left')
    plt.title('Exp')
    plt.xlabel('x Displacement')
    plt.ylabel(('v Disp (m)'))
    fig2.savefig('../doc/Exp.jpeg')

    fig3  = plt.figure(3)
    forplot = np.array([data[2], data[3]])
    for i in range(carCount):
        plt.scatter(forplot[0, i], forplot[1, i], label='mivCar' + str(i), marker='x')
    plt.xlim(-60, 60)
    plt.ylim(-60, 60)
    plt.legend(loc='upper left')
    plt.title('actuals')
    plt.xlabel('x Displacement')
    plt.ylabel(('v Disp (m)'))
    fig3.savefig('../doc/actual.jpeg')

    plt.show()

if __name__ == '__main__':
    microcar(['exp1.csv', 'exp2.csv'], ['act1.csv', 'act2.csv'])
    plotmicrocar(['exp1.csv', 'exp2.csv'], ['act1.csv', 'act2.csv'])
