import math
from collections import Counter
import numpy as np

def bm25_score(query_tokens: list[str], docs: list[list[str]], k1: float = 1.2, b: float = 0.75) -> np.ndarray:
    """
    Returns a NumPy array with one score per document.
    """
    N = len(docs)
    if N == 0:
        return np.array([], dtype=float)
    
    # Calculate document lengths and average document length
    doc_lens = np.array([len(doc) for doc in docs], dtype=float)
    avgdl = np.mean(doc_lens) if N > 0 else 0.0

    # Count term frequencies for each document and document frequencies across corpus
    doc_counters = [Counter(doc) for doc in docs]
    df_counts = Counter()
    for doc in docs:
        df_counts.update(set(doc))

    # Unique query terms ( repeated query terms are counted once )
    unique_query_terms = set(query_tokens)
    
    # Initialize total score vector for each document
    scores = np.zeros(N, dtype=float)

    for term in unique_query_terms:
        # Document frequency df(t)
        df = df_counts.get(term, 0)
        
        # Calculate Inverse Document Frequency (IDF)
        idf = math.log((N - df + 0.5) / (df + 0.5) + 1.0)
        
        # Term frequencies across all documents
        tf = np.array([counter[term] for counter in doc_counters], dtype=float)
        
        # BM25 term score component with length normalization
        numerator = tf * (k1 + 1.0)
        denominator = tf + k1 * (1.0 - b + b * (doc_lens / avgdl))
        
        # Accumulate score per document
        scores += idf * (numerator / denominator)

    return scores