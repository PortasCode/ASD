def topologiczne_sortowanie(G: list[list[int]]):
    n = len(G)
    visited = [False for _ in range(n)]
    result = []

    def dfs(G, u):
        visited[u] = True
        for v in G[u]:
            if visited[v] is not True:
                dfs(G, v)

        result.append(u)

    for u in range(n):
        if not visited[u]:
            dfs(G, u)

    return result[::-1]


def main_function(G: list[list[int]]) -> bool:
    kandydat = topologiczne_sortowanie(G)[0]
    n = len(G)
    visited = [False for _ in range(n)]

    def DFS(G: list[list[int]], u: int):
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                DFS(G, v)

    visited[kandydat] = True
    DFS(G, kandydat)

    return False not in visited
