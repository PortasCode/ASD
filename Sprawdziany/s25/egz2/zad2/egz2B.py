from egz2Btesty import runtests
from math import inf as INF
from collections import deque

"""
Złożoność podstawowa O(n^2) 


def bitgame(T: list[int]):
    result = []
    for liczba in T:
        changed = False

        for i in range(len(result)):
            if result[i] <= liczba:
                changed = True
                result[i] = INF

        if not changed:
            result.append(liczba)

    licznik = 0
    for liczba in result:
        if liczba != INF:
            licznik += 1

    return licznik

"""

"""
Złożoność średnia O(n * logn)
"""


def bin_search(T: list[int], number: int) -> int:
    n = len(T)
    left = 0
    right = n - 1
    wynik = n

    while left <= right:
        mid = (left + right) // 2
        if T[mid] > number:
            left = mid + 1
        else:
            wynik = mid
            right = mid - 1

    return wynik


def bitgame(T: list[int]):
    Q = []

    for liczba in T:
        if not Q:
            Q.append(liczba)
            continue

        indeks = bin_search(Q, liczba)

        if indeks == len(Q):
            Q.append(liczba)
        else:
            del Q[indeks:]

    return len(Q)


"""
Złożoność wzorcowa O(n)

def bitgame(T: list[int]) -> int:
    Q = deque()

    for liczba in T:
        if not Q:
            Q.append(liczba)
        else:
            changed = False
            while Q[-1] <= liczba:
                changed = True
                Q.pop()

            if not changed:
                Q.append(liczba)

    return len(Q)
"""


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(bitgame, all_tests=True)
