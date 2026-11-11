import numpy as np

def e_means(X: list, centroids: list, batches: list, alpha: float) -> dict:
    X = np.array(X, dtype=float)
    C = np.array(centroids, dtype=float)
    
    n, d = X.shape
    k = C.shape[0]
    
    S = C.copy()
    N = np.ones(k, dtype=float)
    
    for batch in batches:
        X_b = X[batch]
        
        dist = ((X_b[:, None, :] - C[None, :, :]) ** 2).sum(axis=-1)
        labels_b = np.argmin(dist, axis=1)
        
        s = np.zeros((k, d), dtype=float)
        np.add.at(s, labels_b, X_b)
        n_b = np.bincount(labels_b, minlength=k).astype(float)
        
        S = (1 - alpha) * S + alpha * s
        N = (1 - alpha) * N + alpha * n_b
        
        mask = N > 0
        C[mask] = S[mask] / N[mask][:, None]
        
    dist_all = ((X[:, None, :] - C[None, :, :]) ** 2).sum(axis=-1)
    labels = np.argmin(dist_all, axis=1)
    mse = float(dist_all[np.arange(n), labels].mean())
    
    return {
        "centroids": C,
        "counts": N,
        "labels": labels,
        "mse": mse
    }