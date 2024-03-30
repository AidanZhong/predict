from typing import List

from cost import cost
from hypothesis import hypothesis
from params import *
import matplotlib.pyplot as plt


def cal_gradient(index: int, x: List[float], y: List[float], z: List[float]) -> float:
    res = 0
    nn = min(x.__len__(), y.__len__(), z.__len__())
    for i in range(nn):
        item = hypothesis(x[i], y[i]) - z[i]
        if index == 0:
            item *= 1
        elif index == 1:
            item *= x[i]
        elif index == 2:
            item *= (x[i] ** 2)
        elif index == 3:
            item *= y[i]
        elif index == 4:
            item *= (y[i] ** 2)
        res += item
    res /= nn
    return res


def train():
    # training all the parameters thetas
    costs = []
    for iter_time in range(ITERATIONS):
        print('iteration ', iter_time, end="\n")
        print(THETA)
        c = cost(x, y, z)
        costs.append(c)
        print('cost is', c)
        for i in range(PARAM_COUNT):
            THETA[i] -= ALPHA * cal_gradient(i, x, y, z)
    plt.plot(range(ITERATIONS), costs)
    plt.xlabel('iterations')
    plt.ylabel('cost')
    plt.title('cost change while iteration')
    plt.grid(True)
    plt.show()
