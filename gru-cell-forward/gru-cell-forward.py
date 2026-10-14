import numpy as np


def gru_cell_forward(x: list, h_prev: list, params: dict) -> np.ndarray:
    x_arr = np.asarray(x, dtype=float)
    h_arr = np.asarray(h_prev, dtype=float)

    is_1d = h_arr.ndim == 1
    if is_1d:
        x_in = x_arr[None, :]
        h_in = h_arr[None, :]
    else:
        x_in = x_arr
        h_in = h_arr

    def sigmoid(a):
        return np.where(
            a >= 0, 1 / (1 + np.exp(-a)), np.exp(a) / (1 + np.exp(a))
        )

    z = sigmoid(
        x_in @ params["Wz"] + h_in @ params["Uz"] + params["bz"]
    )
    r = sigmoid(
        x_in @ params["Wr"] + h_in @ params["Ur"] + params["br"]
    )
    h_tilde = np.tanh(
        x_in @ params["Wh"] + (r * h_in) @ params["Uh"] + params["bh"]
    )

    h_next = (1 - z) * h_in + z * h_tilde

    return h_next.squeeze(axis=0) if is_1d else h_next