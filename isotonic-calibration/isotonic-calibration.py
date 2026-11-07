def calibrate_isotonic(cal_labels: list, cal_probs: list, new_probs: list) -> list:
    sorted_pairs = sorted(zip(cal_probs, cal_labels), key=lambda x: x[0])
    sorted_probs = [p for p, l in sorted_pairs]
    
    blocks = []
    for p, l in sorted_pairs:
        blocks.append({'weight': 1, 'sum': float(l), 'mean': float(l)})
        while len(blocks) >= 2 and blocks[-2]['mean'] > blocks[-1]['mean']:
            b2 = blocks.pop()
            b1 = blocks.pop()
            new_weight = b1['weight'] + b2['weight']
            new_sum = b1['sum'] + b2['sum']
            blocks.append({
                'weight': new_weight,
                'sum': new_sum,
                'mean': new_sum / new_weight
            })
            
    fitted_values = []
    for b in blocks:
        fitted_values.extend([b['mean']] * b['weight'])
        
    n = len(sorted_probs)
    result = []
    
    for x in new_probs:
        if x <= sorted_probs[0]:
            result.append(fitted_values[0])
        elif x >= sorted_probs[-1]:
            result.append(fitted_values[-1])
        else:
            low = 0
            high = n - 1
            idx = 0
            while low <= high:
                mid = (low + high) // 2
                if sorted_probs[mid] <= x:
                    idx = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            if sorted_probs[idx] == x:
                result.append(fitted_values[idx])
            else:
                x0, x1 = sorted_probs[idx], sorted_probs[idx + 1]
                y0, y1 = fitted_values[idx], fitted_values[idx + 1]
                interpolated = y0 + (x - x0) * (y1 - y0) / (x1 - x0)
                result.append(interpolated)
                
    return result