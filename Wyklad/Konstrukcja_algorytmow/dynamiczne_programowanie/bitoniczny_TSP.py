def bitoniczy_TSP(D: list[list[int]]):
    n = len(D)
    F = [[float("inf") for _ in range(n)] for _ in range(n)]

    F[0][1] = D[0][1]

    def f(i, j):
        if F[i][j] != float("inf"):
            return F[i][j]
        if i < j - 1:
            F[i][j] = f(i, j - 1) + D[j - 1][j]
        else:
            for k in range(j - 1):
                F[i][j] = min(F[i][j], f(k, j - 1) + D[k][j])
