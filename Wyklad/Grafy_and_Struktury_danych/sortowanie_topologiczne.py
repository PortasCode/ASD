# Grad musi być DAG - Direct Acyclic Graph
# Złożoność O(V+E)


def topologiczne_sortowanie(G):
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
