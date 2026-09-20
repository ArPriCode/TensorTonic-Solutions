import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model) containing sinusoidal positional encodings.
    """
    # Create position column vector of shape (seq_len, 1)
    pos = np.arange(seq_len)[:, np.newaxis]
    
    # Calculate scale indices i for frequencies: i = 0, 1, ..., ceil(d_model / 2) - 1
    num_freqs = (d_model + 1) // 2
    i = np.arange(num_freqs)
    
    # Compute division term: base^(2i / d_model)
    div_term = base ** ((2 * i) / d_model)
    
    # Compute angles using broadcasting: shape (seq_len, num_freqs)
    angles = pos / div_term
    
    # Initialize output array
    pe = np.zeros((seq_len, d_model), dtype=float)
    
    # Apply sine to even indices and cosine to odd indices
    pe[:, 0::2] = np.sin(angles)
    pe[:, 1::2] = np.cos(angles[:, :d_model // 2])
    
    return pe