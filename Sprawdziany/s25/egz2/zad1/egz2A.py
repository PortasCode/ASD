from egz2Atesty import runtests

"""
Złożoność podstawowa O( D(V+E) )

def DFS(G, start, end, spy):
    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v] and v != spy:
                dfs(v)

    visited = [False] * len(G)
    dfs(start)

    return visited[end]


def kingnqueen(
    V: int, E: list[tuple[int, int]], D: int, K: list[int], Q: list[int], B: list[int]
) -> int:
    G = [[] for _ in range(V)]
    for u, v in E:
        G[u].append(v)
        G[v].append(u)

    result = 0

    for i in range(D):
        start = K[i]
        end = Q[i]
        spy = B[i]

        if DFS(G, start, end, spy):
            result += 1

    return result
"""


def kingnqueen(
    V: int, E: list[tuple[int, int]], D: int, K: list[int], Q: list[int], B: list[int]
) -> int:
    return 0


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kingnqueen, all_tests=True)
