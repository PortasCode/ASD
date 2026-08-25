from egz2btesty import runtests


def magic(C) -> int:
    n = len(C)
    if n == 0:
        return -1

    dp = [-1 for _ in range(n)]
    dp[0] = 0

    for i in range(n):
        if dp[i] == -1:
            continue

        gold = C[i][0]
        doors = C[i][1:]

        for koszt, komnata in doors:
            if komnata == -1:
                continue

            if koszt > gold:
                if dp[i] + gold >= koszt:
                    dp[komnata] = max(dp[komnata], (dp[i] + gold - koszt))

            if gold - 10 <= koszt:
                dp[komnata] = max(dp[komnata], dp[i] + (gold - koszt))

    return dp[n - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=True)
