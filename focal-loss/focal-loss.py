import numpy as np


def focal_loss(p: list, y: list, gamma: float = 2.0) -> float:
    p_arr = np.asarray(p, dtype=np.float64)
    y_arr = np.asarray(y, dtype=np.float64)

    eps = 1e-15
    p_clipped = np.clip(p_arr, eps, 1.0 - eps)

    pos_term = -((1.0 - p_clipped) ** gamma) * y_arr * np.log(p_clipped)
    neg_term = -(p_clipped ** gamma) * (1.0 - y_arr) * np.log1p(-p_clipped)

    loss = pos_term + neg_term
    return float(np.mean(loss))