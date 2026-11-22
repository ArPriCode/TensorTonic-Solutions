def gae(rewards: list, values: list, gamma: float, lam: float) -> list:
    n = len(rewards)
    advantages = [0.0] * n
    last_gae = 0.0
    for t in range(n - 1, -1, -1):
        delta = rewards[t] + gamma * values[t + 1] - values[t]
        last_gae = delta + gamma * lam * last_gae
        advantages[t] = float(last_gae)
    return advantages