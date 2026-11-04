def choose_threshold(y_true: list, scores: list, min_precision: float) -> dict:
    total_positives = sum(y_true)
    if total_positives == 0:
        return {"threshold": None, "precision": None, "recall": None}

    pairs = sorted(zip(scores, y_true), reverse=True)
    best_t, best_p, best_r = None, None, None

    tp = 0
    pp = 0
    n = len(pairs)
    i = 0

    while i < n:
        current_score = pairs[i][0]
        
        while i < n and pairs[i][0] == current_score:
            pp += 1
            tp += pairs[i][1]
            i += 1
            
        precision = tp / pp
        recall = tp / total_positives
        
        if precision >= min_precision:
            if best_r is None or recall > best_r or (recall == best_r and precision > best_p):
                best_t = current_score
                best_p = precision
                best_r = recall
                
    if best_t is None:
        return {"threshold": None, "precision": None, "recall": None}
        
    return {"threshold": float(best_t), "precision": float(best_p), "recall": float(best_r)}