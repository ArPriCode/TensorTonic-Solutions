def lbfgs_direction(grad: list, s_list: list, y_list: list) -> list:
    m = len(s_list)
    n = len(grad)

    rho = []
    for i in range(m):
        ys = sum(y_list[i][j] * s_list[i][j] for j in range(n))
        rho.append(1.0 / ys)

    q = list(grad)
    alpha = [0.0] * m

    for i in range(m - 1, -1, -1):
        sq = sum(s_list[i][j] * q[j] for j in range(n))
        alpha[i] = rho[i] * sq
        for j in range(n):
            q[j] -= alpha[i] * y_list[i][j]

    s_last = s_list[-1]
    y_last = y_list[-1]
    sy = sum(s_last[j] * y_last[j] for j in range(n))
    yy = sum(y_last[j] * y_last[j] for j in range(n))
    gamma = sy / yy

    r = [gamma * q[j] for j in range(n)]

    for i in range(m):
        yr = sum(y_list[i][j] * r[j] for j in range(n))
        beta = rho[i] * yr
        for j in range(n):
            r[j] += s_list[i][j] * (alpha[i] - beta)

    return [-r[j] for j in range(n)]