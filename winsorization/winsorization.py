import math

def winsorize(values: list, lower_pct: float, upper_pct: float) -> list:
    n = len(values)
    if n == 0:
        return []

    sorted_vals = sorted(values)

    def get_percentile_bound(p):
        k = (n - 1) * p / 100.0
        lower_idx = math.floor(k)
        upper_idx = math.ceil(k)
        if lower_idx == upper_idx:
            return float(sorted_vals[lower_idx])
        weight = k - lower_idx
        return sorted_vals[lower_idx] + weight * (sorted_vals[upper_idx] - sorted_vals[lower_idx])

    lower_bound = get_percentile_bound(lower_pct)
    upper_bound = get_percentile_bound(upper_pct)

    return [max(lower_bound, min(upper_bound, v)) for v in values]