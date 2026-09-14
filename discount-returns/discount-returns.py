def discount_returns(rewards: list, gamma: float) -> list:
    """
    Returns the discounted return at every timestep.
    """
    T = len(rewards)
    returns = [0.0] * T
    running_return = 0.0

    for t in reversed(range(T)):
        running_return = float(rewards[t]) + gamma * running_return
        returns[t] = running_return

    return returns