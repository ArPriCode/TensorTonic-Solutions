import math

def binning(values: list, num_bins: int) -> list:
    min_val = min(values)
    max_val = max(values)
    
    if min_val == max_val:
        return [0] * len(values)
        
    w = (max_val - min_val) / num_bins
    
    result = []
    for x in values:
        bin_idx = math.floor((x - min_val) / w)
        result.append(min(bin_idx, num_bins - 1))
        
    return result