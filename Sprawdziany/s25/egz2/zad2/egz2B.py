from egz2Btesty import runtests
from math import inf as INF
from collections import deque


def bitgame(T):
    n = len(T)
    Q = deque()

    for i in range(n):
        if len(Q) == 0:
            Q.append(T[i])
            continue

        removed = False
        while len(Q) > 0 and Q[-1] <= T[i]:
            removed = True
            Q.pop()

        if not removed:
            Q.append(T[i])

    return len(Q)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(bitgame, all_tests=True)
