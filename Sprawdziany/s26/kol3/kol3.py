from kol3_test import runtests

"""
Złożoność podstawowa O(ZN^2)
"""


"""
Złożoność lepsza O(TN)
"""


def transactions(M: int, T: list[tuple[int, int, int, int]]) -> int:
    max_czas = 0
    for _, czas, _, _ in T:
        max_czas = max(max_czas, czas)

    dp = [0] * (max_czas + 1)
    dp[0] = M

    for czas in range(1, max_czas + 1):
        dp[czas] = dp[czas - 1]

        for krotka in T:
            if krotka[1] == czas:
                if dp[krotka[0] - 1] >= krotka[2]:
                    dp[czas] = max(
                        dp[czas], dp[krotka[0] - 1] + (krotka[3] - krotka[2])
                    )

    return dp[max_czas]


"""
Złożoność lepsza O(N^2+T)
"""
"""
Złożoność wzorcowa O(T+NlogN)


def transactions(M: int, T: list[tuple[int, int, int, int]]) -> int:
    T.sort(key=lambda x: x[1])
    maksymalny_czas = T[-1][1]
    wskaznik_tablica = 0

    dp = [0] * (maksymalny_czas + 1)
    dp[0] = M

    for i in range(1, maksymalny_czas + 1):
        dp[i] = dp[i - 1]

        while wskaznik_tablica < len(T) and i == T[wskaznik_tablica][1]:
            if dp[T[wskaznik_tablica][0] - 1] >= T[wskaznik_tablica][2]:
                dp[i] = max(
                    dp[i],
                    dp[T[wskaznik_tablica][0] - 1]
                    + (T[wskaznik_tablica][3] - T[wskaznik_tablica][2]),
                )
            wskaznik_tablica += 1

    return dp[maksymalny_czas]
"""

"""
Złożoność wzorcowa O(T+N)


def counting_sort(
    T: list[tuple[int, int, int, int]], max_czas: int
) -> list[tuple[int, int, int, int]]:
    n = len(T)
    B = [(0, 0, 0, 0) for _ in range(n)]
    C = [0] * (max_czas + 1)

    for krotka in T:
        C[krotka[1]] += 1

    for i in range(1, max_czas + 1):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        krotka = T[i]
        C[krotka[1]] -= 1
        B[C[krotka[1]]] = krotka
    return B


def transactions(M: int, T: list[tuple[int, int, int, int]]) -> int:
    max_czas = 0
    for _, czas, _, _ in T:
        max_czas = max(max_czas, czas)
    T = counting_sort(T, max_czas)

    dp = [0] * (max_czas + 1)
    dp[0] = M
    wskaznik_tablica = 0

    for i in range(1, max_czas + 1):
        dp[i] = dp[i - 1]

        while wskaznik_tablica < len(T) and i == T[wskaznik_tablica][1]:
            if dp[T[wskaznik_tablica][0] - 1] >= T[wskaznik_tablica][2]:
                dp[i] = max(
                    dp[i],
                    dp[T[wskaznik_tablica][0] - 1]
                    + (T[wskaznik_tablica][3] - T[wskaznik_tablica][2]),
                )
            wskaznik_tablica += 1
    return dp[max_czas]

"""

runtests(transactions, all_tests=True)
