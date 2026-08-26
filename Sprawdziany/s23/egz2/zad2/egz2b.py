from egz2btesty import runtests


def parking(X: list[int], Y: list[int]):
    n = len(X)
    m = len(Y)

    dp = [[float("inf") for _ in range(m)] for _ in range(n)]

    dp[0][0] = abs(X[0] - Y[0])
    for k in range(1, m):
        dp[0][k] = min(dp[0][k - 1], abs(X[0] - Y[k]))

    for i in range(1, n):
        for j in range(i, m):
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1] + abs(X[i] - Y[j]))

    return dp[n - 1][m - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)
