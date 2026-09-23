import numpy as np

def rmsprop_step(
    w: list,
    g: list,
    s: list,
    lr: float = 0.001,
    beta: float = 0.9,
    eps: float = 1e-8,
) -> tuple[list, list]:
    """
    Returns (new_w, new_s) with the same shapes as the inputs.
    """
    # Convert inputs to NumPy arrays
    w_arr = np.array(w, dtype=float)
    g_arr = np.array(g, dtype=float)
    s_arr = np.array(s, dtype=float)
    
    # Step 1: Update Running Average of Squared Gradients
    new_s = beta * s_arr + (1 - beta) * (g_arr ** 2)
    
    # Step 2: Parameter Update
    new_w = w_arr - (lr / (np.sqrt(new_s) + eps)) * g_arr
    
    # Return updated values as Python lists matching the input format
    return new_w.tolist(), new_s.tolist()