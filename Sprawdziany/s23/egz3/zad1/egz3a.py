from egz3atesty import runtests
from queue import PriorityQueue

"""
Złożoność wzorcowa O(n^2)
"""


def goodknight(G: list[list[int]], s: int, t: int):
    n = len(G)
    dist = [[float("inf") for _ in range(17)] for _ in range(n)]
    dist[s][0] = 0
    pq = PriorityQueue()

    for i in range(n):
        if G[s][i] != -1:
            pq.put((G[s][i], G[s][i], i))
            dist[i][G[s][i]] = G[s][i]

    while not pq.empty():
        cost, hours, vert = pq.get()

        if dist[vert][hours] < cost:
            continue

        if vert == t:
            return cost

        for child in range(n):
            if G[vert][child] != -1:
                child_cost = G[vert][child]

                # nie da się dojechać bez odpoczunku
                if hours + child_cost > 16:
                    if dist[child][child_cost] > cost + 8 + child_cost:
                        pq.put((cost + 8 + child_cost, child_cost, child))
                        dist[child][child_cost] = cost + 8 + child_cost
                else:
                    if dist[child][child_cost + hours] > cost + child_cost:
                        dist[child][hours + child_cost] = cost + child_cost
                        pq.put((cost + child_cost, hours + child_cost, child))

                    if dist[child][child_cost] > cost + 8 + child_cost:
                        dist[child][child_cost] = cost + 8 + child_cost
                        pq.put((cost + 8 + child_cost, child_cost, child))

    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(goodknight, all_tests=True)
