import sys
sys.path.append('./lib')

from tools import microcar, plotmicrocar

if __name__ == '__main__':
    microcar(['exp1.csv', 'exp2.csv'], ['act1.csv', 'act2.csv'])
    plotmicrocar(['exp1.csv', 'exp2.csv'], ['act1.csv', 'act2.csv'])
