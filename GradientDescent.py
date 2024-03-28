from typing import List

from hypothesis import hypothesis


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
