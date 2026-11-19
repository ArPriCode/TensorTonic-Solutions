import math


def elu(x: list, alpha: float = 1.0) -> list:
  return [float(val) if val > 0 else float(alpha * (math.exp(val) - 1)) for val in x]