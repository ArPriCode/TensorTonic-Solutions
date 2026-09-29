import numpy as np

def triplet_loss(anchor: list, positive: list, negative: list, margin: float = 1.0) -> float:
    """
    Returns the loss as a float.
    """
    anchor = np.asarray(anchor)
    positive = np.asarray(positive)
    negative = np.asarray(negative)

    pos_dist = np.sum((anchor - positive) ** 2, axis=-1)
    neg_dist = np.sum((anchor - negative) ** 2, axis=-1)

    loss = np.maximum(0, pos_dist - neg_dist + margin)

    return float(np.mean(loss))