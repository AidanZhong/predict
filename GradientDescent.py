from typing import List

from cost import cost
from hypothesis import hypothesis
from params import ITERATIONS, THETA, ALPHA, PARAM_COUNT


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


# training all the parameters thetas
x = []
y = []
z = []
for iter_time in range(ITERATIONS):
    print('iteration ', iter_time, end="\n")
    print(THETA)
    for i in range(PARAM_COUNT):
        THETA[i] -= ALPHA * cal_gradient(i, x, y, z)
    print('cost is', cost(x, y, z))
