from collections import defaultdict

def rank_transform(values: list[float]) -> list[float]:
    val_to_indices = defaultdict(list)
    for idx, val in enumerate(values):
        val_to_indices[val].append(idx)
    
    ranks = [0.0] * len(values)
    current_pos = 1  
    
    for val in sorted(val_to_indices.keys()):
        indices = val_to_indices[val]
        count = len(indices)
        avg_rank = (2 * current_pos + count - 1) / 2.0
        
        for idx in indices:
            ranks[idx] = avg_rank
            
        current_pos += count
        
    return ranks