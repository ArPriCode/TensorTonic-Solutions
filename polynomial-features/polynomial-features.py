def polynomial_features(values: list, degree: int) -> list:
    return [[x**d for d in range(degree + 1)] for x in values]