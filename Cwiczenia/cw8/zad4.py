def skaczaca_zaba(T: list[int]):
    n = len(T)

    dp = [[-1 for _ in range(n)] for _ in range(n)]

    dp[0][0] = T[0]

    for i in range(1, n):
        for j in range(1, n):
            for m in range(j - 1, -1, -1):
                if dp[i - 1][m] == -1:
                    continue

                odleglosc = j - m
                if odleglosc**2 <= dp[i - 1][m]:
                    nowa_odleglosc = dp[i - 1][m] - odleglosc**2 + T[j]
                    if nowa_odleglosc > dp[i][j]:
                        dp[i][j] = nowa_odleglosc

                        if j == n - 1:
                            return i
    return -1
