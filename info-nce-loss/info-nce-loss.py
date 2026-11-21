import numpy as np

def info_nce_loss(Z1: list, Z2: list, temperature: float = 0.1) -> float:
    z1 = np.asarray(Z1, dtype=np.float64)
    z2 = np.asarray(Z2, dtype=np.float64)
    
    logits = (z1 @ z2.T) / temperature
    shifted = logits - np.max(logits, axis=1, keepdims=True)
    
    exp_shifted = np.exp(shifted)
    log_sum_exp = np.log(np.sum(exp_shifted, axis=1))
    pos_logits = np.diag(shifted)
    
    loss = -np.mean(pos_logits - log_sum_exp)
    return float(loss)