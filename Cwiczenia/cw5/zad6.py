def dfs(G: list[list[int]], W: list[list[int]], x: int, y: int):

    def DFSvisit(u, last_weight):
        if u == y:
            return True

        for v in G[u]:
            current_weight = W[u][v]
            if current_weight < last_weight and current_weight > weights[v]:
                weights[v] = current_weight
                if DFSvisit(v, current_weight):
                    return True
        return False

    N = len(G)
    weights = [-1] * N
    DFSvisit(x, float("inf"))
