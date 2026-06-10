def orchard(T: list[int], m: int) -> int | float:
    n = len(T)
    dp = [[float("inf") for _ in range(m)] for _ in range(n)]

    if T[0] % m == 0:
        dp[0][0] = 0
    else:
        dp[0][0] = 1

    for j in range(1, m):
        if T[0] % m == j:
            dp[0][j] = 0

    for i in range(1, n):
        for j in range(m):
            opcja_wyciecia = dp[i - 1][j] + 1

            prev_j = (j - T[i]) % m
            opcja_zostawienia = dp[i - 1][prev_j]
            dp[i][j] = min(opcja_wyciecia, opcja_zostawienia)
    return dp[n - 1][0]
