def gae(rewards: list, values: list, gamma: float, lam: float) -> list:
    n = len(rewards)
    advantages = [0.0] * n
    gae_acc = 0.0
    for t in reversed(range(n)):
        delta = rewards[t] + gamma * values[t + 1] - values[t]
        gae_acc = delta + gamma * lam * gae_acc
        advantages[t] = float(gae_acc)
    return advantages