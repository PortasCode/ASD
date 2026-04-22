from collections import deque


def BFS(G: list[list[int]], s: int):
    N = len(G)
    Q = deque()
    d = [-1 for _ in range(N)]
    visited = [False for _ in range(N)]
    parent = [None for _ in range(N)]

    d[s] = 0
    visited[s] = True

    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1

    return d, visited, parent
