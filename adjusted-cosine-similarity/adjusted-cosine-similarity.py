import math

def adjusted_cosine_similarity(ratings_matrix: list, item_i: int, item_j: int) -> float:
    """
    Returns the adjusted cosine similarity between the requested items.
    """
    # Step 1: Compute user mean ratings from all nonzero (rated) entries per user
    user_means = []
    for row in ratings_matrix:
        rated_vals = [val for val in row if val != 0]
        if rated_vals:
            user_means.append(sum(rated_vals) / len(rated_vals))
        else:
            user_means.append(0.0)

    num_sum = 0.0
    denom_i = 0.0
    denom_j = 0.0

    # Step 2: Iterate over users who have rated BOTH item_i and item_j
    for u, row in enumerate(ratings_matrix):
        r_ui = row[item_i]
        r_uj = row[item_j]

        # Include only users who rated both requested items
        if r_ui != 0 and r_uj != 0:
            u_mean = user_means[u]
            
            # Center ratings around the user's mean
            diff_i = r_ui - u_mean
            diff_j = r_uj - u_mean

            num_sum += diff_i * diff_j
            denom_i += diff_i ** 2
            denom_j += diff_j ** 2

    # Step 3: Compute denominator and handle zero division
    denominator = math.sqrt(denom_i) * math.sqrt(denom_j)
    if denominator == 0.0:
        return 0.0

    return num_sum / denominator