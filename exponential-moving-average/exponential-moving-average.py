def exponential_moving_average(values: list, alpha: float) -> list:
    if not values:
        return []

    ema = [values[0]]
    for t in range(1, len(values)):
        current_ema = alpha * values[t] + (1 - alpha) * ema[t - 1]
        ema.append(current_ema)

    return ema