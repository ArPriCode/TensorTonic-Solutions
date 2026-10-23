def conv2d(
    image: list, kernel: list, stride: int = 1, padding: int = 0
) -> list:
    H, W = len(image), len(image[0])
    Kh, Kw = len(kernel), len(kernel[0])

    padded_H = H + 2 * padding
    padded_W = W + 2 * padding

    padded_image = [[0] * padded_W for _ in range(padded_H)]
    for r in range(H):
        for c in range(W):
            padded_image[r + padding][c + padding] = image[r][c]

    H_out = (H + 2 * padding - Kh) // stride + 1
    W_out = (W + 2 * padding - Kw) // stride + 1

    output = []
    for i in range(H_out):
        row = []
        for j in range(W_out):
            val = 0
            for a in range(Kh):
                for b in range(Kw):
                    val += (
                        padded_image[i * stride + a][j * stride + b]
                        * kernel[a][b]
                    )
            row.append(val)
        output.append(row)

    return output