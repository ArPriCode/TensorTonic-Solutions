def min_max_scaling(data: list) -> list:
    rows = len(data)
    cols = len(data[0])
    result = [[0.0] * cols for _ in range(rows)]
    
    for j in range(cols):
        col_vals = [data[i][j] for i in range(rows)]
        min_val = min(col_vals)
        max_val = max(col_vals)
        denom = max_val - min_val
        
        if denom != 0:
            for i in range(rows):
                result[i][j] = (data[i][j] - min_val) / denom
                
    return result