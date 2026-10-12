def popularity_ranking(items: list, min_votes: int, global_mean: float) -> list:
    return [
        (v / (v + min_votes)) * R + (min_votes / (v + min_votes)) * global_mean
        for R, v in items
    ]