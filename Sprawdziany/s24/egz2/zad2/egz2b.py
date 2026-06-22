from egz2btesty import runtests
from collections import deque


def tory_amos(E, A, B):
    n = 0
    for u, v, _, _ in E:
        n = max(n, u, v)

    n += 1
    G = [[] for _ in range(n)]

    #           I             P
    dist = [[float("inf"), float("inf")] for _ in range(n)]

    for u, v, cost, tp in E:
        G[u].append((v, cost, tp))
        G[v].append((u, cost, tp))

    Q = deque()
    Q.append((A, 0, 0, ""))

    while Q:
        vert, delay, total_cost, tp = Q.popleft()

        if tp == "":
            for child, child_cost, child_tp in G[vert]:
                Q.append((child, child_cost - 1, child_cost, child_tp))
            continue

        if tp == "I":
            pomocnicza = 0
        else:
            pomocnicza = 1

        if delay > 0:
            if dist[vert][pomocnicza] > total_cost:
                Q.append((vert, delay - 1, total_cost, tp))
            continue

        if total_cost >= dist[vert][pomocnicza]:
            continue

        dist[vert][pomocnicza] = total_cost

        if vert == B:
            return total_cost

        if vert == B:
            return total_cost

        for child, child_cost, child_tp in G[vert]:
            if child_tp == tp:
                if tp == "I":
                    kara = 5
                else:  # tp == 'P'
                    kara = 10
            else:
                kara = 20

            Q.append(
                (child, child_cost + kara - 1, total_cost + child_cost + kara, child_tp)
            )

    return None


runtests(tory_amos, all_tests=True)
