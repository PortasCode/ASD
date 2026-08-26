from egz1Atesty import runtests
from queue import PriorityQueue


def dijkstra(G: list[list[tuple[int, int]]], start: int, is_robbed: bool, r: int = 0):
    n = len(G)
    dist = [float("inf") for _ in range(n)]

    pq = PriorityQueue()
    pq.put((0, start))
    dist[start] = 0

    while not pq.empty():
        cost, vert = pq.get()

        if cost > dist[vert]:
            continue

        for child, child_cost in G[vert]:
            if is_robbed:
                edge_cost = (child_cost * 2) + r
            else:
                edge_cost = child_cost

            total_cost = cost + edge_cost

            if total_cost < dist[child]:
                dist[child] = total_cost
                pq.put((total_cost, child))

    return dist


def gold(G: list[list[tuple[int, int]]], V: list[int], s: int, t: int, r: int):
    dystans_uczciwosc = dijkstra(G, s, is_robbed=False)

    dystans_kradziez = dijkstra(G, t, is_robbed=True, r=r)

    result = float("inf")
    for idx, robbery in enumerate(V):
        cost = dystans_uczciwosc[idx] + dystans_kradziez[idx] - robbery
        result = min(result, cost)

    return result


runtests(gold, all_tests=True)
