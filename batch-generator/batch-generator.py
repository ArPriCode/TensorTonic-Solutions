import numpy as np


def batch_generator(
    X: list,
    y: list,
    batch_size: int,
    seed: int = 42,
    drop_last: bool = False,
):
    """Returns a generator of (X_batch, y_batch) tuples."""
    X_arr = np.asarray(X)
    y_arr = np.asarray(y)

    n_samples = len(X_arr)
    rng = np.random.default_rng(seed)

    indices = np.arange(n_samples)
    rng.shuffle(indices)

    for i in range(0, n_samples, batch_size):
        batch_indices = indices[i : i + batch_size]

        if drop_last and len(batch_indices) < batch_size:
            break

        yield X_arr[batch_indices], y_arr[batch_indices]