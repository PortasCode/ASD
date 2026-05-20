def problem_plecakowy(P: list[float], W: list[int], B: int):
    n = len(P)
    F: list[list[float | int]] = [[0 for _ in range(B + 1)] for _ in range(n)]

    for b in range(W[0], B + 1):
        F[0][b] = P[0]

    for i in range(1, n):
        for b in range(B + 1):
            F[i][b] = F[i - 1][b]
            if b >= W[i]:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])

    return F[n - 1][B]
