from params import theta


def hypothesis(maintain_time: float, temperature: float) -> float:
    const_item = theta[0]
    maintain_item = theta[1] * maintain_time + theta[2] * (maintain_time ** 2)
    temperature_item = theta[3] * temperature + theta[4] * (temperature ** 2)
    hyp = const_item + maintain_item + temperature_item
    return hyp
