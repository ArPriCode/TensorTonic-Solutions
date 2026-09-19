def retraining_policy(daily_stats: list, config: dict) -> list:
    """
    Returns a list of retraining day numbers.
    """
    retrain_days = []
    
    # State tracking variables
    budget = config["budget"]
    retrain_cost = config["retrain_cost"]
    cooldown = config["cooldown"]
    max_staleness = config["max_staleness"]
    drift_threshold = config["drift_threshold"]
    performance_threshold = config["performance_threshold"]
    
    # Initialize last_retrain_day so the initial cooldown is satisfied on day 1
    last_retrain_day = float('-inf')
    days_since_retrain = 0

    for stat in daily_stats:
        day = stat["day"]
        drift_score = stat["drift_score"]
        performance = stat["performance"]
        
        # Increment staleness at the start of each day
        days_since_retrain += 1
        
        # Check if any trigger condition requests retraining
        requested = (
            drift_score > drift_threshold or
            performance < performance_threshold or
            days_since_retrain >= max_staleness
        )
        
        # Check if operational constraints allow retraining
        cooldown_met = (last_retrain_day == float('-inf')) or ((day - last_retrain_day) >= cooldown)
        budget_met = budget >= retrain_cost
        
        # Retrain if requested and both constraints are satisfied
        if requested and cooldown_met and budget_met:
            retrain_days.append(day)
            last_retrain_day = day
            days_since_retrain = 0
            budget -= retrain_cost

    return retrain_days