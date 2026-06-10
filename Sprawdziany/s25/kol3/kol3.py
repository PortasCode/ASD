from kol3testy import runtests


def parkiet(B: list[list[int]], C: list[list[int]], s: int) -> int | float:
    n = len(B)
    m = len(B[0])
    dp = [[float("inf") for _ in range(m)] for _ in range(n)]
    dp[0][0] = 0

    min_ciecia = float("inf")  # Zmienna na trzymanie najlepszego wyniku

    for i in range(n):
        for j in range(m):
            if dp[i][j] == float("inf"):
                continue

            if i == n - 1 or j == m - 1:
                if C[i][j] <= s:
                    min_ciecia = min(min_ciecia, dp[i][j])

            if i + 1 < n:
                if C[i][j] - C[i + 1][j] <= s:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)

            if j + 1 < m:
                if C[i][j] - C[i][j + 1] <= s:
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

    if min_ciecia == float("inf"):
        return -1
    return min_ciecia


# runtests(parkiet, all_tests=True)


def parkiet_zachlanny(B: list[list[int]], C: list[list[int]], s: int) -> int | float:
    n = len(B)
    m = len(B[0])

    def symulacja(priorytet_poziom: bool) -> int | float:
        i, j = 0, 0
        while i < n and j < m:
            if C[i][j] <= s:
                return i + j + min(n - 1 - i, m - 1 - j)

            mozna_poziom = i + 1 < n and C[i][j] - C[i + 1][j] <= s
            mozna_pion = j + 1 < m and C[i][j] - C[i][j + 1] <= s

            if priorytet_poziom:
                if mozna_poziom:
                    i += 1
                elif mozna_pion:
                    j += 1
                else:
                    return float("inf")
            else:
                if mozna_pion:
                    j += 1
                elif mozna_poziom:
                    i += 1
                else:
                    return float("inf")

        return float("inf")

    wynik = min(symulacja(True), symulacja(False))

    if wynik == float("inf"):
        return -1
    return wynik


runtests(parkiet_zachlanny, all_tests=True)
