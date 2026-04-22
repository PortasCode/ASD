# mam tutaj napisać algortym BFS, ktory znajdzie najkrotsza sciezke do jakiegos wierzcholka
# a następnie będzie możliwe wypisanie jego trasy z powrtoem
from collections import deque


# Złożoność to O(V+E) tak jak każdego BFS
def BFS(G: list[list[int]], s: int) -> None:
    Q = deque()
    n = len(G)
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]

    Q.append(s)
    d[s] = 0
    visited[s] = True

    while Q:
        u = Q.popleft()

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.append(v)
