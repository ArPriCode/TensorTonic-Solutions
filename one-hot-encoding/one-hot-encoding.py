import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    y_arr = np.array(y)
    if num_classes is None:
        num_classes = np.max(y_arr) + 1
        
    encoded = np.zeros((len(y_arr), num_classes), dtype=float)
    encoded[np.arange(len(y_arr)), y_arr] = 1.0
    
    return encoded