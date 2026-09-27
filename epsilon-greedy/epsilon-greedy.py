import numpy as np

def epsilon_greedy(q_values: list, epsilon: float, seed: int = 0) -> int:
    rng = np.random.default_rng(seed)

    u = rng.random()

    if u < epsilon:
        return int(rng.integers(len(q_values)))
    else:
        return int(np.argmax(q_values))