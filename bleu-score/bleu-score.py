import math
from collections import Counter

def bleu_score(candidate: list, reference: list, max_n: int) -> float:
    c = len(candidate)
    r = len(reference)
    
    if c == 0:
        return 0.0

    p_n = []
    
    for n in range(1, max_n + 1):
        if c < n:
            return 0.0
            
        cand_ngrams = Counter(tuple(candidate[i:i+n]) for i in range(c - n + 1))
        ref_ngrams = Counter(tuple(reference[i:i+n]) for i in range(r - n + 1))
        
        clipped_matches = 0
        total_cand_ngrams = 0
        
        for ngram, count in cand_ngrams.items():
            total_cand_ngrams += count
            clipped_matches += min(count, ref_ngrams.get(ngram, 0))
            
        if total_cand_ngrams == 0 or clipped_matches == 0:
            return 0.0
            
        p_n.append(clipped_matches / total_cand_ngrams)

    if c >= r:
        bp = 1.0
    else:
        bp = math.exp(1 - r / c)

    log_sum = sum(math.log(p) for p in p_n)
    
    return bp * math.exp(log_sum / max_n)