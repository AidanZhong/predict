from params import theta


def hypothesis(x: float) -> float:
    hyp = 0
    for i in range(theta.__len__()):
        hyp += theta[i] * pow(x, i)
    return hyp
