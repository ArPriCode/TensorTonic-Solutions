import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    
    n_samples, n_features = X.shape
    w = np.zeros(n_features, dtype=float)
    b = 0.0
    
    for _ in range(steps):
        z = X @ w + b
        p = _sigmoid(z)
        
        error = p - y
        grad_w = (X.T @ error) / n_samples
        grad_b = np.mean(error)
        
        w -= lr * grad_w
        b -= lr * grad_b
        
    return w, float(b)