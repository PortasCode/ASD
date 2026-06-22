from egz2Atesty import runtests
from collections import deque


"""
def bfs(G, V, king, queen, spy):
    visited = [False for _ in range(V)]
    visited[king] = True

    kopia_zapasowa = G[spy]
    G[spy] = []

    Q = deque()
    Q.append(king)

    while len(Q) > 0:
        u = Q.popleft()

        for v in G[u]:
            if v == spy:
                continue

            if not visited[v]:
                visited[v] = True
                Q.append(v)

    G[spy] = kopia_zapasowa
    return visited[queen]


def kingnqueen(
    V: int, E: list[tuple[int, int]], D: int, K: list[int], Q: list[int], B: list[int]
):
    G = [[] for _ in range(V)]

    for u, v in E:
        G[u].append(v)
        G[v].append(u)

    dostarczone_listy = 0

    for dzien in range(D):
        if bfs(G, V, K[dzien], Q[dzien], B[dzien]):
            dostarczone_listy += 1

    return dostarczone_listy

"""


def kingnqueen(
    V: int, E: list[tuple[int, int]], D: int, K: list[int], Q: list[int], B: list[int]
):
    G = [[] for _ in range(V)]
    for u, v in E:
        G[u].append(v)
        G[v].append(u)

    visited = [False] * V
    tin = [0] * V
    low = [0] * V
    timer = 0

    stack = []
    components = []
    is_ap = [False] * V

    def dfs(u, parent=-1):
        nonlocal timer
        visited[u] = True
        timer += 1
        tin[u] = low[u] = timer
        children = 0

        for v in G[u]:
            if v == parent:
                continue
            if visited[v]:
                low[u] = min(low[u], tin[v])
                if tin[v] < tin[u]:
                    stack.append((u, v))
            else:
                children += 1
                stack.append((u, v))
                dfs(v, u)
                low[u] = min(low[u], low[v])

                if low[v] >= tin[u]:
                    if parent != -1:
                        is_ap[u] = True

                    comp = set()
                    while True:
                        edge = stack.pop()
                        comp.add(edge[0])
                        comp.add(edge[1])
                        if edge == (u, v):
                            break
                    components.append(comp)

        if parent == -1 and children > 1:
            is_ap[u] = True

    dfs(0)

    BCT_V = V + len(components)
    BCT_adj = [[] for _ in range(BCT_V)]
    bcc_id = [-1] * V

    for i, comp in enumerate(components):
        bcc_node = V + i
        for node in comp:
            if is_ap[node]:
                BCT_adj[bcc_node].append(node)
                BCT_adj[node].append(bcc_node)
            else:
                bcc_id[node] = bcc_node

    def get_bct_id(node):
        return node if is_ap[node] else bcc_id[node]

    successful_days = 0

    for i in range(D):
        start = get_bct_id(K[i])
        target = get_bct_id(Q[i])
        spy = B[i]

        if start == target:
            successful_days += 1
            continue

        vis = [False] * BCT_V
        if is_ap[spy]:
            vis[spy] = True

        q_bfs = deque([start])
        vis[start] = True

        reached = False
        while q_bfs:
            curr = q_bfs.popleft()
            if curr == target:
                reached = True
                break
            for nxt in BCT_adj[curr]:
                if not vis[nxt]:
                    vis[nxt] = True
                    q_bfs.append(nxt)

        if reached:
            successful_days += 1

    return successful_days


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kingnqueen, all_tests=False)
