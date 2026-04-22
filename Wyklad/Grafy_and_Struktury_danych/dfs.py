def DFS(G):
    def DFSvisit(G, u):
        nonlocal time

        d1[u] = time
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSvisit(G, v)

        d2[u] = time
        time += 1

    N = len(G)
    d1 = [-1 for _ in range(N)]
    d2 = [-1 for _ in range(N)]
    visited = [False for _ in range(N)]
    parent = [None for _ in range(N)]

    time = 0

    for u in range(N):
        if not visited[u]:
            DFSvisit(G, u)

    return d1, d2, visited, parent
