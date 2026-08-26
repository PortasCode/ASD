from zadSiEtesty import runtests

"""
Złożoność akceptowalna O(NT^2)


def sale_i_egzaminy(E: list[tuple[int, int, int]]):
    n = len(E)
    if n == 0:
        return 0

    maksymalny_czas = E[-1][1]

    dp = [
        [
            [-float("inf") for _ in range(maksymalny_czas + 1)]
            for _ in range(maksymalny_czas + 1)
        ]
        for _ in range(n + 1)
    ]
    dp[0][0][0] = 0

    for i in range(n):
        idx = i + 1
        start, koniec, liczba_studentow = E[i]

        for t1 in range(maksymalny_czas + 1):
            for t2 in range(maksymalny_czas + 1):
                if dp[idx - 1][t1][t2] == -float("inf"):
                    continue

                dp[idx][t1][t2] = max(dp[idx][t1][t2], dp[idx - 1][t1][t2])
                if t1 < start:
                    dp[idx][koniec][t2] = max(
                        dp[idx][koniec][t2], dp[idx - 1][t1][t2] + liczba_studentow
                    )

                if t2 < start:
                    dp[idx][t1][koniec] = max(
                        dp[idx][t1][koniec], dp[idx - 1][t1][t2] + liczba_studentow
                    )

    result = 0
    for t1 in range(maksymalny_czas + 1):
        for t2 in range(maksymalny_czas + 1):
            if dp[n][t1][t2] > result:
                result = dp[n][t1][t2]

    return result
"""

"""
Złożoność wzorcowa O(N^3)
"""


def sale_i_egzaminy(E: list[tuple[int, int, int]]):
    n = len(E)
    if n == 0:
        return 0

    E = [(0, 0, 0)] + E

    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            for k in range(i):
                if dp[k][j] != -1:
                    if E[k][1] < E[i][0]:
                        dp[i][j] = max(dp[i][j], dp[k][j] + E[i][2])
                if dp[j][k] != -1:
                    if E[k][1] < E[i][0]:
                        dp[j][i] = max(dp[j][i], dp[j][k] + E[i][2])

    result = -1

    for i in range(n + 1):
        for j in range(n + 1):
            if result < dp[i][j]:
                result = dp[i][j]

    return result


runtests(sale_i_egzaminy, all_tests=True)
