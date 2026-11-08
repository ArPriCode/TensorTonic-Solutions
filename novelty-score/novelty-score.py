import math


def novelty_score(
    recommendations: list, item_counts: list, n_users: int
) -> float:
    if not recommendations:
        return 0.0

    total_novelty = sum(
        -math.log2(item_counts[item] / n_users) for item in recommendations
    )
    return total_novelty / len(recommendations)