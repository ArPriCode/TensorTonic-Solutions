import numpy as np

def td_value_update(
    V: list, 
    s: int, 
    r: float, 
    s_next: int, 
    alpha: float, 
    gamma: float
) -> np.ndarray:
    """
    Returns a NumPy array with the updated state value for state `s` using TD(0).
    """
    # Create a copy as a floating-point NumPy array to avoid mutating the input
    V_updated = np.array(V, dtype=float).copy()
    
    # Calculate Temporal Difference (TD) error: delta = r + gamma * V(s_next) - V(s)
    delta = r + gamma * V_updated[s_next] - V_updated[s]
    
    # Update state value for state s: V_new(s) = V(s) + alpha * delta
    V_updated[s] += alpha * delta
    
    return V_updated