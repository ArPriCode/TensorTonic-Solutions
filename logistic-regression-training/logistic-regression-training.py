import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """ Returns elementwise sigmoid values. """
    return np.where(z >= 0, 1 / (1 + np.exp(-z)), np.exp(z) / (1 + np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """ Returns the trained weights and bias as (w, b). """
    N, D = X.shape
    
    # Initialize weights w as zeros and bias b as 0.0
    w = np.zeros(D)
    b = 0.0
    
    for _ in range(steps):
        # Linear combination: z = Xw + b
        z = X @ w + b
        
        # Predicted probabilities: p = sigmoid(z)
        p = _sigmoid(z)
        
        # Gradients of Binary Cross-Entropy Loss w.r.t weights and bias
        dw = (X.T @ (p - y)) / N
        db = np.mean(p - y)
        
        # Gradient descent update step
        w -= lr * dw
        b -= lr * db
        
    return w, float(b)