import numpy as np

def knn_distance(X_train: list, X_test: list, k: int) -> np.ndarray:
    train = np.asarray(X_train, dtype=float)
    test = np.asarray(X_test, dtype=float)
    
    if train.ndim == 1:
        train = train.reshape(-1, 1)
    if test.ndim == 1:
        test = test.reshape(-1, 1)
        
    n_train = train.shape[0]
    n_test = test.shape[0]
    
    if n_train == 0:
        return np.full((n_test, k), -1, dtype=int)
        
    diffs = test[:, None, :] - train[None, :, :]
    dists = np.linalg.norm(diffs, axis=-1)
    sorted_indices = np.argsort(dists, axis=1, kind='stable').astype(int)
    
    if k <= n_train:
        return sorted_indices[:, :k]
        
    padding = np.full((n_test, k - n_train), -1, dtype=int)
    return np.concatenate([sorted_indices, padding], axis=1)