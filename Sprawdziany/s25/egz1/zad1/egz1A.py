from egz1Atesty import runtests
from collections import deque

"""
Złożoność O( (n+m)log(n+m) ) 

def battle_DP(P: list[int], K: list[int], R: list[int]) -> int:
    n = len(K)

    T = []
    for punkt in P:
        T.append((punkt, -1))
    for i in range(n):
        T.append((K[i], R[i]))
    T.sort()

    Q = deque()
    result = 0
    for wspolrzedne, zasieg in T:
        if zasieg != -1:
            Q.append((wspolrzedne, zasieg))
        else:
            while Q:
                armata, pocisk = Q.pop()
                if armata + pocisk >= wspolrzedne:
                    result += 1
                    break
    return result
"""

"""
Złożoność wzorcowa O( n+m )
"""


def counting_sort(A: list[tuple[int, int]]):
    n = len(A)
    m = 4 * n + 1
    B: list[tuple[int, int]] = [(0, 0)] * n
    C = [0] * m

    for i in range(n):
        C[A[i][0]] += 1

    for i in range(1, m):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[A[i][0]] -= 1
        B[C[A[i][0]]] = A[i]

    return B


def battle_DP(P: list[int], K: list[int], R: list[int]) -> int:
    n = len(K)
    T = []
    for punkt in P:
        T.append((punkt, -1))

    for i in range(n):
        T.append((K[i], R[i]))

    T = counting_sort(T)
    Q = deque()

    result = 0
    for wspolrzedne, zasieg in T:
        if zasieg != -1:
            Q.append((wspolrzedne, zasieg))
            continue
        else:
            while Q:
                armata, pocisk = Q.pop()
                if armata + pocisk >= wspolrzedne:
                    result += 1
                    break
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(battle_DP, all_tests=True)
