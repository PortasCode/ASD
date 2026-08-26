from egz1btesty import runtests


def planets(D: list[int], C: list[int], T: list[tuple[int, int]], E: int):
    n = len(D)
    dp = [[float("inf") for _ in range(E + 1)] for _ in range(n)]
    dp[0][0] = 0

    for i in range(1, E + 1):
        dp[0][i] = dp[0][i - 1] + C[0]

    if T[0][0] != 0:
        dp[T[0][0]][0] = T[0][1]

    for i in range(1, n):
        for e in range(E + 1):
            # sprawdzenie czy da się dolecieć mając z wcześniejszej planety mając tyle paliwa
            odlegosc = D[i] - D[i - 1]
            if e + odlegosc <= E:
                dp[i][e] = min(dp[i - 1][e + odlegosc], dp[i][e])

            # sprawdzenie czy bardizej nie opłacalne jest zatankowanie do takiej ilości paliwa
            if e > 0:
                dp[i][e] = min(dp[i][e], dp[i][e - 1] + C[i])

            # sprawdzenie czy użycie teleportu jest możliwe i opłacalne
            if e == 0 and dp[i][e] != float("inf"):
                if T[i][0] != i:
                    dp[T[i][0]][0] = min(dp[T[i][0]][0], dp[i][0] + T[i][1])

    return min(dp[n - 1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
