import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    X_arr = np.array(X, dtype=float)
    N = X_arr.shape[0]
    
    # Center the data by subtracting column means
    centered = X_arr - np.mean(X_arr, axis=0)
    
    # Compute sample covariance matrix
    cov = (centered.T @ centered) / (N - 1)
    
    # Calculate feature standard deviations (ddof=1 for sample std)
    std = np.sqrt(np.diag(cov))
    
    # Outer product of standard deviations creates denominator matrix
    outer_std = np.outer(std, std)
    
    # Division by zero variance automatically results in np.nan (with warning suppressed)
    with np.errstate(divide='ignore', invalid='ignore'):
        corr = cov / outer_std
        
    return corr