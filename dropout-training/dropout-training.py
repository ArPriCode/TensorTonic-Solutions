import numpy as np


def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:
    x_arr = np.asarray(x)
    if p == 1.0:
        dropout_pattern = np.zeros_like(x_arr, dtype=float)
        output = np.zeros_like(x_arr, dtype=float)
        return output, dropout_pattern

    if rng is not None:
        rand_vals = rng.random(x_arr.shape)
    else:
        rand_vals = np.random.random(x_arr.shape)

    mask = rand_vals < (1.0 - p)
    dropout_pattern = mask.astype(float) / (1.0 - p)
    output = x_arr * dropout_pattern
    return output, dropout_pattern