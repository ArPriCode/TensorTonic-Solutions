def double_exponential_smoothing(series: list, alpha: float, beta: float) -> list:
    """
    Returns the smoothed level at every time step.
    """
    if not series:
        return []
    
    # Initialize level and trend
    level = series[0]
    trend = series[1] - series[0] if len(series) > 1 else 0
    
    levels = [level]
    
    for t in range(1, len(series)):
        y_t = series[t]
        
        # Update level using previous level and trend
        prev_level = level
        level = alpha * y_t + (1 - alpha) * (prev_level + trend)
        
        # Update trend using new level and previous level
        trend = beta * (level - prev_level) + (1 - beta) * trend
        
        levels.append(level)
        
    return levels