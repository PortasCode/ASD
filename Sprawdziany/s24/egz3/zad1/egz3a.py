from egz3atesty import runtests
from collections import deque


def mykoryza(G: list[list[int]], T: list[int], d: int):
    n = len(G)
    Q = deque()

    k = len(T)
    for i in range(k):
        #        vert,grzyb,czas
        Q.append((T[i], i, 0))

    #           time            grzyb
    dist: list[list[int | float]] = [[float("inf"), float("inf")] for _ in range(n)]
    while Q:
        vert, grzyb, czas = Q.popleft()

        if czas > dist[vert][0]:
            continue

        if dist[vert][0] == float("inf"):
            dist[vert] = [czas, grzyb]
        elif dist[vert][0] == czas:
            dist[vert][1] = min(dist[vert][1], grzyb)

        for child in G[vert]:
            if dist[child][0] == float("inf"):
                Q.append((child, grzyb, czas + 1))

    counter = 0
    for i in range(n):
        if dist[i][1] == d:
            counter += 1

    return counter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(mykoryza, all_tests=True)
