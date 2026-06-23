from egz3atesty import runtests
from queue import PriorityQueue


def goodknight(G: list[list[int]], s: int, t: int):
    n = len(G)
    T: list[list[tuple[int, int]]] = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if G[i][j] != -1:
                T[i].append((j, G[i][j]))

    dist = [[float("inf") for _ in range(17)] for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0, s, 16))

    while not pq.empty():
        cost, vert, power = pq.get()

        if cost > dist[vert][power]:
            continue

        if vert == t:
            return cost

        # zawsze moze sie przespac w zamku
        if power < 16:
            if dist[vert][16] > cost + 8:
                dist[vert][16] = cost + 8
                pq.put((cost + 8, vert, 16))

        for child, child_cost in T[vert]:
            remain_power = power - child_cost

            if remain_power < 0:
                continue

            if dist[child][remain_power] > cost + child_cost:
                dist[child][remain_power] = cost + child_cost
                pq.put((cost + child_cost, child, remain_power))

    return


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(goodknight, all_tests=True)
