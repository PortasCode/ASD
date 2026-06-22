from egz1Btesty import runtests
from math import inf as INF


"""
Złożoność tego pomysłu to jest O( E(V+E) ), czyli dla każdej krawędzi odpalenie BFS lub DFS


def dfs_zadanie(V: int, E: list[tuple[int, int]], indeks: int) -> bool:
    liczba_krawedzi = len(E)
    G = [[] for _ in range(V)]
    startowy_wierzcholek = -1
    koncowy_wierzcholek = 0

    for i in range(liczba_krawedzi):
        if i == indeks:
            startowy_wierzcholek = E[i][0]
            koncowy_wierzcholek = E[i][1]
            continue

        u, v = E[i]
        G[u].append(v)

    visited = [False for _ in range(V)]

    def dfs_visit(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G, v)

    dfs_visit(G, startowy_wierzcholek)

    return visited[koncowy_wierzcholek]


def critical(V: int, E: list[tuple[int, int]]):
    liczba_krawedzi = len(E)
    result = 0

    for indeks in range(liczba_krawedzi):
        if not dfs_zadanie(V, E, indeks):
            result += 1

    return result

"""

"""
To zaadanie polega na zbudowaniu macierzy, wskazującej czy da się jakkolwiek przejść z wierzchołka A do B przez jakiś inny wierzchołek lub bezpośrednio
( jest to algorytm Flloyda - Warshalla )

nastepnie sprawdzam kazda krawedz i rozważam czy da się przejść z wierzchołka u do v ale nie przez krawędź u -> v


def critical_v2(V: int, E: list[tuple[int, int]]):
    M = [[False for _ in range(V)] for _ in range(V)]

    for i in range(V):
        M[i][i] = True

    for u, v in E:
        M[u][v] = True

    for k in range(V):
        for i in range(V):
            for j in range(V):
                M[i][j] = M[i][k] and M[k][j]

    result = 0
    for u, v in E:
        visited = False

        for k in range(V):
            if k == u or k == v:
                continue
            if M[u][k] and M[k][v]:
                visited = True
                break

        if not visited:
            result += 1

    return result

"""


def critical_v3(V: int, E: list[tuple[int, int]]):
    G: list[list[int]] = [[] for _ in range(V)]

    for u, v in E:
        G[u].append(v)

    T = [[] for _ in range(V)]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical_v2, all_tests=True)
