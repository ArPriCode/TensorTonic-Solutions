def differencing(series: list, order: int) -> list:
    res = list(series)
    for _ in range(order):
        res = [res[i] - res[i - 1] for i in range(1, len(res))]
    return res