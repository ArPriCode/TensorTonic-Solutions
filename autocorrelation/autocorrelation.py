def autocorrelation(series: list, max_lag: int) -> list:
    """
    Returns normalized autocorrelation from lag zero through max_lag.
    """
    n = len(series)
    
    # Step 1: Compute mean
    mean = sum(series) / n
    
    # Mean-center the series
    centered = [x - mean for x in series]
    
    # Step 2: Compute lag-zero variance (gamma_0)
    gamma_0 = sum(x ** 2 for x in centered)
    
    # Handle zero variance edge case
    if gamma_0 == 0:
        res = [0.0] * (max_lag + 1)
        res[0] = 1.0
        return res
    
    # Step 3: Compute normalized autocorrelation for each lag
    result = []
    for k in range(max_lag + 1):
        cov_k = sum(centered[t] * centered[t + k] for t in range(n - k))
        r_k = round(cov_k / gamma_0, 6)
        result.append(r_k)
        
    return result