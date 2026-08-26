from egz3atesty import runtests
from collections import deque


def mykoryza(G: list[list[int]], T: list[int], d: int):
    n = len(G)
    Q = deque()
    visited = [-1] * n
    arrived = [float("inf")] * n

    for idx, vert in enumerate(T):
        Q.append((vert, idx))
        arrived[vert] = 0
        visited[vert] = idx

    while Q:
        vert, wirus = Q.popleft()

        for child in G[vert]:
            if arrived[vert] + 1 < arrived[child]:
                visited[child] = wirus
                arrived[child] = arrived[vert] + 1
                Q.append((child, wirus))

    return visited.count(d)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(mykoryza, all_tests=True)
