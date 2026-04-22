from collections import deque


def bfs(G: list[list[tuple[int, int]]], s: int, t: int) -> int | float:
    N = len(G)
    visited = [False for _ in range(N)]
    d = [float("inf") for _ in range(N)]
    Q = deque()

    Q.append(s)
    visited[s] = True
    d[s] = 0

    while Q:
        u = Q.popleft()

        if u == t:
            break

        for v, koszt in G[u]:
            nowy_koszt = d[u] + koszt

            if nowy_koszt < d[v]:
                d[v] = nowy_koszt

                if koszt == 0:
                    Q.appendleft(v)
                else:
                    Q.append(v)

    return d[t] if d[t] != float("inf") else -1
