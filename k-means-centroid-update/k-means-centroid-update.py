def k_means_centroid_update(points: list, assignments: list, k: int) -> list:
    if not points:
        return []
    
    dim = len(points[0])
    sums = [[0.0] * dim for _ in range(k)]
    counts = [0] * k
    
    for point, cluster_idx in zip(points, assignments):
        counts[cluster_idx] += 1
        for d in range(dim):
            sums[cluster_idx][d] += point[d]
            
    centroids = []
    for j in range(k):
        if counts[j] == 0:
            centroids.append([0.0] * dim)
        else:
            centroids.append([sums[j][d] / counts[j] for d in range(dim)])
            
    return centroids