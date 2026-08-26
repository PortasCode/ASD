from egz3Btesty import runtests
from math import inf as INF


def kom(X: list[int], Z: list[int], W: int):
    n = len(X)
    dp = [[-INF for _ in range(W + 1)] for _ in range(n + 1)]
    dp[0][W] = 0

    for plansza in range(1, n + 1):
        idx = plansza - 1
        for zycie in range(W + 1):
            dp[plansza][zycie] = dp[plansza - 1][zycie]

            # udział w wyścigu
            if zycie + Z[idx] <= W:
                dp[plansza][zycie] = max(
                    dp[plansza][zycie], dp[plansza - 1][zycie + Z[idx]] + X[idx]
                )

            # udział w spa
            if zycie - Z[idx] >= 0:
                if dp[plansza - 1][zycie - Z[idx]] - X[idx] >= 0:
                    dp[plansza][zycie] = max(
                        dp[plansza][zycie], dp[plansza - 1][zycie - Z[idx]] - X[idx]
                    )

    return max(dp[n])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kom, all_tests=True)
