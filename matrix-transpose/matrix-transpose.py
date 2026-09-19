import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    N = len(A)
    M = len(A[0])
    
    # Initialize an output array of shape (M, N)
    transposed = np.zeros((M, N), dtype=type(A[0][0]) if N and M else float)
    
    # Populate the transposed array manually
    for i in range(N):
        for j in range(M):
            transposed[j][i] = A[i][j]
            
    return transposed