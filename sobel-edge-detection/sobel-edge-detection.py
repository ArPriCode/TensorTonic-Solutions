import math

def sobel_edges(image: list) -> list:
    """
    Returns the zero-padded Sobel gradient magnitude at every pixel.
    """

    h = len(image)
    w = len(image[0])

    Kx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]

    Ky = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]

    # Zero-padded image
    padded = [[0] * (w + 2) for _ in range(h + 2)]

    for i in range(h):
        for j in range(w):
            padded[i + 1][j + 1] = image[i][j]

    result = [[0.0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            gx = 0
            gy = 0

            for a in range(3):
                for b in range(3):
                    pixel = padded[i + a][j + b]
                    gx += Kx[a][b] * pixel
                    gy += Ky[a][b] * pixel

            result[i][j] = math.sqrt(gx * gx + gy * gy)

    return result