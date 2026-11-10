import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    X_np = np.array(X, dtype=np.float64)
    y_np = np.array(y, dtype=np.float64)
    
    X_T = X_np.T
    w = np.linalg.inv(X_T @ X_np) @ X_T @ y_np
    
    return w.tolist()