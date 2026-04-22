def dfs(G: list[list[int]]):

    def dfsvisit(G: list[list[int]], u: int):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfsvisit(G, v)
        result.append(u)

    n = len(G)
    visited = [False for _ in range(n)]
    result = []
    dfsvisit(G, 0)
    return result
