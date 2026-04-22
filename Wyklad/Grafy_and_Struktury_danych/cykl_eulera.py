# to coś dziala tylko dla grafow skierowanych i jest to O(v+E)
def euler(G):
    n = len(G)
    idx = [0 for _ in range(n)]
    cycle = []

    def dfsvisit(v: int):
        while idx[v] < len(G[v]):
            u = G[v][idx[v]]
            idx[v] += 1
            if idx[u] >= len(G[u]) or G[u][idx[u]] > v:
                continue
            dfsvisit(u)
        cycle.append(v)

    dfsvisit(0)
    return cycle


# to jest zlożoność O(V^2)
def euler_brut(G):
    n = len(G)
    deleted_verts = [[False for _ in range(n)] for _ in range(n)]
    cycle = []

    def dfs(G: list[list[int]], u: int):
        for v in G[u]:
            min_v = min(u, v)
            max_v = max(u, v)

            if not deleted_verts[min_v][max_v]:
                deleted_verts[min_v][max_v] = True
                dfs(G, v)

        cycle.append(u)

    dfs(G, 0)
    return cycle[::-1]
