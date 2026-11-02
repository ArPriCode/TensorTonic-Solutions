from collections import Counter


def frequency_encoding(values: list) -> list:
    counts = Counter(values)
    n = len(values)
    return [counts[val] / n for val in values]