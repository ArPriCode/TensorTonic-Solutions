import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:

    x = np.asarray(x, dtype=float)

    if rng is None:
        random_values = np.random.random(x.shape)
    else:
        random_values = rng.random(x.shape)

    scale = 1 / (1 - p)

    mask = (random_values >= p).astype(float)

    dropout_pattern = mask * scale
    output = x * dropout_pattern

    return output, dropout_pattern