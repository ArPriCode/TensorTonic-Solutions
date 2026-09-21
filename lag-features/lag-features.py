def lag_features(series: list, lags: list) -> list:
    """
    Returns the lag feature matrix.
    """
    max_lag = max(lags)
    result = []
    
    # Start at the maximum lag so every referenced observation exists in bounds
    for t in range(max_lag, len(series)):
        row = [series[t - lag] for lag in lags]
        result.append(row)
        
    return result