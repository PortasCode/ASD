from egz3Btesty import runtests
from math import inf as INF


def kom(X, Z, W):
    n = len(X)

    dp: list[list[float | int]] = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for j in range(W):
        dp[0][j] = -float("inf")

    for i in range(1, n + 1):
        for j in range(W + 1):
            # nie robie nic
            dp[i][j] = dp[i - 1][j]

            # podejmuje walke na tej planszy
            zdrowie = j + Z[i - 1]
            if zdrowie <= W:
                dp[i][j] = max(dp[i][j], dp[i - 1][zdrowie] + X[i - 1])

            # probuje se odpoczac
            zdrowie = j - Z[i - 1]
            if zdrowie >= 0 and dp[i - 1][zdrowie] >= X[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][zdrowie] - X[i - 1])

    najwiekszy_wynik = 0
    for j in range(W + 1):
        najwiekszy_wynik = max(najwiekszy_wynik, dp[n][j])

    return najwiekszy_wynik


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kom, all_tests=True)
