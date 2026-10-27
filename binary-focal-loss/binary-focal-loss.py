import math


def binary_focal_loss(
    predictions: list, targets: list, alpha: float, gamma: float
) -> float:
    total_loss = 0.0
    n = len(predictions)

    for p, y in zip(predictions, targets):
        p_t = p if y == 1 else (1.0 - p)
        fl = -alpha * ((1.0 - p_t) ** gamma) * math.log(p_t)
        total_loss += fl

    return total_loss / n