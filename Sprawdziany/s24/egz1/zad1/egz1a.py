from egz1atesty import runtests
from queue import PriorityQueue


def dijkstra(G: list[list[tuple[int, int]]], s: int):
    n = len(G)
    dist = [float("inf") for _ in range(n)]
    dist[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        cost, vert = pq.get()

        if cost > dist[vert]:
            continue

        for child, child_cost in G[vert]:
            if cost + child_cost < dist[child]:
                dist[child] = cost + child_cost
                pq.put((cost + child_cost, child))

    return dist


def armstrong(
    B: list[tuple[int, int, int]], G: list[tuple[int, int, int]], s: int, t: int
) -> int:
    n = -1
    for u, v, _ in G:
        n = max(n, u, v)
    for u, _, _ in B:
        n = max(n, u)
    n += 1

    NG = [[] for _ in range(n)]
    for u, v, w in G:
        NG[u].append((v, w))
        NG[v].append((u, w))

    dystans_s = dijkstra(NG, s)
    dystans_t = dijkstra(NG, t)

    result = dystans_s[t]

    for u, p, q in B:
        if dystans_s[u] != float("inf") and dystans_t[u] != float("inf"):
            kandydat = int(dystans_s[u] + dystans_t[u] * (p / q))
            result = min(kandydat, result)

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(armstrong, all_tests=True)
