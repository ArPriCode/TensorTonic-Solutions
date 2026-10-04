import math

def rotate_image(image: list, angle_degrees: float) -> list:
    h = len(image)
    w = len(image[0])

    cy = (h - 1) / 2
    cx = (w - 1) / 2

    theta = angle_degrees * math.pi / 180
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)

    result = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            dy = i - cy
            dx = j - cx

            sy = cy + dy * cos_t + dx * sin_t
            sx = cx - dy * sin_t + dx * cos_t

            sy = round(sy)
            sx = round(sx)

            if 0 <= sy < h and 0 <= sx < w:
                result[i][j] = image[sy][sx]

    return result