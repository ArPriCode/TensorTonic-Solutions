import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    arr = np.array(X, dtype=float, copy=True)

    if arr.ndim == 1:
        mask = np.isnan(arr)

        if np.all(mask):
            arr[:] = 0.0
        else:
            value = np.mean(arr[~mask]) if strategy == "mean" else np.median(arr[~mask])
            arr[mask] = value

        return arr

    for j in range(arr.shape[1]):
        mask = np.isnan(arr[:, j])

        if np.all(mask):
            arr[:, j] = 0.0
        else:
            value = np.mean(arr[~mask, j]) if strategy == "mean" else np.median(arr[~mask, j])
            arr[mask, j] = value

    return arr