"""
432101 Mateusz Portka

Złożoność obliczeniowa algorytmu: O(nlogk)
Złożonośc pamięciowa algorytmu: O(k)

Opis działania algorytmu:
    1) Przechodzę po każdym elemencie w tablicy T  - O(n)
        2) każdy element dodaje do kopca (max-kopiec przechowujący k-najmniejszych elementow w tablicy T[:i+1])  - O(logk)
        3) jeżeli w kopcu jest więcej niż k elementów, to zamieniam ostatni element z pierwszym elementem (największym), usuwam największy z kopca
           i naprawiam kopiec - O(logk)
        4) jeżeli największy z najmniejszych elementów jest >= x to uaktualniam wynik - O(1)
    5) zwracam wynik - O(1)

Obliczenia złożoności:
O(n(2logk)) -> O(nlogk)
"""

from zadKTtesty import runtests


def parent(i: int):
    return (i - 1) // 2


def left(i: int):
    return i * 2 + 1


def right(i: int):
    return i * 2 + 2


def element_gora(T):
    idx = len(T) - 1

    while idx > 0:
        rodzic = parent(idx)
        if T[rodzic] < T[idx]:
            T[rodzic], T[idx] = T[idx], T[rodzic]
            idx = rodzic
        else:
            break


def naprawa_kopca(A):
    n = len(A)
    idx = 0

    while idx < n:
        max_idx = idx
        if left(idx) < n and A[left(idx)] > A[max_idx]:
            max_idx = left(idx)
        if right(idx) < n and A[right(idx)] > A[max_idx]:
            max_idx = right(idx)

        if max_idx != idx:
            A[max_idx], A[idx] = A[idx], A[max_idx]
            idx = max_idx
        else:
            break


def kth(T: list[int], x: int, k: int):
    n = len(T)
    kopiec = []
    result = -1

    for i in range(n):
        kopiec.append(T[i])
        element_gora(kopiec)

        if len(kopiec) > k:
            kopiec[0], kopiec[k] = kopiec[k], kopiec[0]
            kopiec.pop()
            naprawa_kopca(kopiec)

        if kopiec[0] >= x:
            result = i

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kth, all_tests=True)
