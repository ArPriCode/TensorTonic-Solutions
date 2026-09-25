def mean_rating_imputation(ratings_matrix: list, mode: str) -> list:
    n = len(ratings_matrix)
    m = len(ratings_matrix[0])

    result = [row[:] for row in ratings_matrix]

    if mode == "user":
        for i in range(n):
            values = [x for x in ratings_matrix[i] if x != 0]
            mean = sum(values) / len(values) if values else 0.0

            for j in range(m):
                if ratings_matrix[i][j] == 0:
                    result[i][j] = mean

    else:
        for j in range(m):
            values = [
                ratings_matrix[i][j]
                for i in range(n)
                if ratings_matrix[i][j] != 0
            ]
            mean = sum(values) / len(values) if values else 0.0

            for i in range(n):
                if ratings_matrix[i][j] == 0:
                    result[i][j] = mean

    return result