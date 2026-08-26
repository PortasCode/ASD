from egz2atesty import runtests

"""
Złożoność podstawowa O(2^n * poly(n)) 

from functools import cache


def wired(T: list[int]):
    n = len(T)

    @cache
    def solve(a: int):
        # Warunek stopu: wszystkie n bitów jest zapalonych
        if a == (1 << n) - 1:
            return 0

        # 1. Znajdź PIERWSZE wolne wejście (pierwsze zero w masce)
        i = 0
        while (a & (1 << i)) != 0:
            i += 1

        result = float("inf")
        empty_between = 0

        # 2. Szukamy pary dla wejścia i
        for j in range(i + 1, n):
            # Jeśli wejście j jest wolne
            if (a & (1 << j)) == 0:
                # Jeśli pomiędzy i oraz j jest parzysta liczba wolnych wejść
                if empty_between % 2 == 0:
                    # TWORZYMY DWA NIEZALEŻNE PODPROBLEMY

                    # Podproblem 1: Wnętrze kabla (wszystko poza i...j staje się "zajęte")
                    inner_mask = a
                    for k in range(n):
                        if k <= i or k >= j:
                            inner_mask |= 1 << k

                    # Podproblem 2: Zewnętrze kabla (wszystko wewnątrz i...j staje się "zajęte")
                    outer_mask = a
                    for k in range(i, j + 1):
                        outer_mask |= 1 << k

                    # Obliczamy koszt i dodajemy wyniki niezależnie rozwiązanych masek
                    koszt_kabla = 1 + abs(T[i] - T[j])
                    koszt_calkowity = (
                        koszt_kabla + solve(inner_mask) + solve(outer_mask)
                    )

                    result = min(result, koszt_calkowity)

                empty_between += 1

        return result
    return solve(0)
"""
"""
Złożonośc wzorcowa O(n^3)
"""


def wired(T: list[int]):

    memo = {}

    def solve(L: int, R: int) -> int:
        if L > R:
            return 0

        if (L, R) in memo:
            return memo[(L, R)]

        if (R - L + 1) % 2 != 0:
            return float("inf")

        result = float("inf")

        for k in range(L + 1, R + 1, 2):
            koszt_kabla = 1 + abs(T[L] - T[k])

            koszt_calkowity = koszt_kabla + solve(L + 1, k - 1) + solve(k + 1, R)

            result = min(result, koszt_calkowity)

        memo[(L, R)] = result
        return result

    return solve(0, len(T) - 1)


def wired_2d(T: list[int]):
    N = len(T)

    dp = [[float("inf")] * N for _ in range(N)]

    for length in range(2, N + 1, 2):
        for L in range(N - length + 1):
            R = L + length - 1  # Prawy koniec przedziału

            for k in range(L + 1, R + 1, 2):
                koszt_kabla = 1 + abs(T[L] - T[k])

                wewnatrz = dp[L + 1][k - 1] if (L + 1 <= k - 1) else 0

                zewnatrz = dp[k + 1][R] if (k + 1 <= R) else 0

                koszt_calkowity = koszt_kabla + wewnatrz + zewnatrz
                dp[L][R] = min(dp[L][R], koszt_calkowity)

    return dp[0][N - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wired, all_tests=True)
