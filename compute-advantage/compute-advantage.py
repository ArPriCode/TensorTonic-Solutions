import numpy as np


def compute_advantage(
    states: list, rewards: list, V: list, gamma: float
) -> np.ndarray:
    rewards_arr = np.asarray(rewards, dtype=float)
    values_arr = np.asarray(V, dtype=float)
    states_arr = np.asarray(states, dtype=int)

    returns = np.zeros_like(rewards_arr, dtype=float)
    running = 0.0
    for i in range(len(rewards_arr) - 1, -1, -1):
        running = rewards_arr[i] + gamma * running
        returns[i] = running

    advantages = returns - values_arr[states_arr]
    return np.round(advantages, 4)