from params import THETA


def hypothesis(maintain_time: float, temperature: float) -> float:
    const_item = THETA[0]
    maintain_item = THETA[1] * maintain_time + THETA[2] * (maintain_time ** 2)
    temperature_item = THETA[3] * temperature + THETA[4] * (temperature ** 2)
    hyp = const_item + maintain_item + temperature_item
    return hyp
