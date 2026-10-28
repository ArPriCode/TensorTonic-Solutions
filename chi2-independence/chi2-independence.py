import numpy as np


def chi2_independence(C: list) -> dict:
    O = np.array(C, dtype=float)
    row_totals = O.sum(axis=1)
    col_totals = O.sum(axis=0)
    grand_total = O.sum()

    expected = np.outer(row_totals, col_totals) / grand_total
    chi2 = float(np.sum((O - expected) ** 2 / expected))

    return {"chi2": chi2, "expected": expected}