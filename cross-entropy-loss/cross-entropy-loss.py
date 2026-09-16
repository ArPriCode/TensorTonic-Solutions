import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    y_true_arr = np.array(y_true)
    y_pred_arr = np.array(y_pred)
    
    # Advanced indexing to select the probability assigned to the true class for each sample
    correct_class_probs = y_pred_arr[np.arange(len(y_true_arr)), y_true_arr]
    
    # Calculate negative log loss and return the mean as a Python float
    return float(-np.mean(np.log(correct_class_probs)))