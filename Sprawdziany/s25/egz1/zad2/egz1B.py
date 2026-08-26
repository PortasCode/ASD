from egz1Btesty import runtests
from math import inf as INF
from collections import deque

"""
Złożonośc podstawowa O(E(V+E))


def bfs(G: list[list[int]], a: int, b: int) -> int:
    n = len(G)
    visited = [False] * n
    Q = deque()
    Q.append(a)
    visited[a] = True

    while Q:
        u = Q.popleft()

        for v in G[u]:
            if u == a and v == b:
                continue

            if not visited[v]:
                visited[v] = True
                Q.append(v)

    return int(not visited[b])


def critical(V: int, E: list[tuple[int, int]]) -> int:
    G = [[] for _ in range(V)]
    for u, v in E:
        G[u].append(v)

    result = 0
    for u, v in E:
        result += bfs(G, u, v)

    return result

"""
"""
ZŁożoność średnia O(V^3) 


def critical(V: int, E: list[tuple[int, int]]) -> int:
    D = [[False for _ in range(V)] for _ in range(V)]
    for i in range(V):
        D[i][i] = True
    for u, v in E:
        D[u][v] = True

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if D[i][k] and D[k][j]:
                    D[i][j] = True

    result = 0
    for u, v in E:
        D[u][v] = False

        for k in range(V):
            if D[u][k] and D[k][v]:
                D[u][v] = True
                break

        if not D[u][v]:
            D[u][v] = True
            result += 1

    return result

"""

"""
ZŁożoność wzorcowa O(EV + V^2)
"""


def bfs(G: list[list[int]], V: int) -> list[list[bool]]:
    D = [[] for _ in range(V)]

    for u in range(V):
        Q = deque()
        Q.append(u)
        visited = [False] * V
        visited[u] = True

        while Q:
            v = Q.popleft()

            for vert in G[v]:
                if not visited[vert]:
                    Q.append(vert)
                    visited[vert] = True

        D[u] = visited

    return D


def critical(V: int, E: list[tuple[int, int]]) -> int:
    G = [[] for _ in range(V)]

    for u, v in E:
        G[u].append(v)

    D = bfs(G, V)

    result = 0
    for u, v in E:
        D[u][v] = False

        for k in range(V):
            if D[u][k] and D[k][v]:
                D[u][v] = True
                break

        if not D[u][v]:
            D[u][v] = True
            result += 1

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests=True)
