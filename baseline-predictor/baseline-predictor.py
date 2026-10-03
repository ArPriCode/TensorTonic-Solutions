def baseline_predict(ratings_matrix: list, target_pairs: list) -> list:
    total = 0
    count = 0

    for row in ratings_matrix:
        for x in row:
            if x != 0:
                total += x
                count += 1

    mu = total / count

    user_bias = []
    for row in ratings_matrix:
        values = [x for x in row if x != 0]
        user_bias.append(sum(values) / len(values) - mu if values else 0)

    cols = len(ratings_matrix[0])
    item_bias = []

    for j in range(cols):
        values = [
            ratings_matrix[i][j]
            for i in range(len(ratings_matrix))
            if ratings_matrix[i][j] != 0
        ]
        item_bias.append(sum(values) / len(values) - mu if values else 0)

    return [
        mu + user_bias[u] + item_bias[i]
        for u, i in target_pairs
    ]