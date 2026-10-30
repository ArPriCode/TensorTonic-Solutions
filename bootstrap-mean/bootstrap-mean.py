import numpy as np


def bootstrap_mean(
    x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0
) -> dict:
    arr = np.asarray(x)
    rng = np.random.default_rng(seed)

    indices = rng.integers(0, arr.size, size=(n_bootstrap, arr.size))
    resample_means = arr[indices].mean(axis=1)

    bootstrap_mean_val = float(np.mean(resample_means))
    alpha = (1.0 - ci) / 2.0
    lower_val = float(np.quantile(resample_means, alpha))
    upper_val = float(np.quantile(resample_means, 1.0 - alpha))

    return {
        "bootstrap_mean": bootstrap_mean_val,
        "lower": lower_val,
        "upper": upper_val,
    }