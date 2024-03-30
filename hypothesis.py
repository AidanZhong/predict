from params import THETA


def hypothesis(x: float, y: float) -> float:
    const_item = THETA[0]
    maintain_item = THETA[1] * x + THETA[2] * (x ** 2)
    temperature_item = THETA[3] * y + THETA[4] * (y ** 2)
    hyp = const_item + maintain_item + temperature_item
    return hyp
