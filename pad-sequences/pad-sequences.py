import numpy as np


def pad_sequences(
    seqs: list, pad_value: int = 0, max_len: int | None = None
) -> np.ndarray:
    """Pads or truncates a list of sequences to a uniform length.

    Returns:
        np.ndarray of shape (N, L) where: N = len(seqs) L = max_len if provided
        else max(len(seq) for seq in seqs) or 0
    """
    if not seqs:
        return np.empty((0, 0), dtype=int)

    if max_len is None:
        max_len = max((len(seq) for seq in seqs), default=0)

    # Initialize matrix with the padding value
    padded_matrix = np.full((len(seqs), max_len), fill_value=pad_value, dtype=int)

    # Fill in each row with the sequence contents up to max_len
    for i, seq in enumerate(seqs):
        length = min(len(seq), max_len)
        padded_matrix[i, :length] = seq[:length]

    return padded_matrix