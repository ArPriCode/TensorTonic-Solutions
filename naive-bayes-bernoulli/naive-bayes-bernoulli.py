import numpy as np

def naive_bayes_bernoulli(X_train: list, y_train: list, X_test: list) -> np.ndarray:
    X_tr = np.asarray(X_train, dtype=np.float64)
    y_tr = np.asarray(y_train)
    X_te = np.asarray(X_test, dtype=np.float64)
    
    classes, class_counts = np.unique(y_tr, return_counts=True)
    log_priors = np.log(class_counts / len(y_tr))
    
    feature_counts = np.array([X_tr[y_tr == c].sum(axis=0) for c in classes])
    theta = (feature_counts + 1.0) / (class_counts[:, None] + 2.0)
    
    log_theta = np.log(theta)
    log_one_minus_theta = np.log1p(-theta)
    
    return log_priors + X_te @ log_theta.T + (1.0 - X_te) @ log_one_minus_theta.T