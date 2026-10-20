import numpy as np


def angle_between_3d(v: list, w: list) -> float:
    v_arr = np.array(v, dtype=float)
    w_arr = np.array(w, dtype=float)

    norm_v = np.linalg.norm(v_arr)
    norm_w = np.linalg.norm(w_arr)

    if norm_v == 0 or norm_w == 0:
        return np.nan

    dot_product = np.dot(v_arr, w_arr)
    cosine = dot_product / (norm_v * norm_w)
    cosine_clamped = np.clip(cosine, -1.0, 1.0)

    return float(np.arccos(cosine_clamped))