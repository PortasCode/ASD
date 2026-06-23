from egz1Atesty import runtests
from queue import PriorityQueue


def gold(G: list[list[tuple[int, int]]], V: list[int], s: int, t: int, r: int):
    n = len(G)
    dist = [[float("inf") for _ in range(n + 1)] for _ in range(n)]

    pq = PriorityQueue()

    # koszt, wierzcholek, nie_ukradl / ukradl
    pq.put((0, s, n))
    dist[s][n] = 0
    result = float("inf")

    while not pq.empty():
        cost, vert, id_zamku = pq.get()

        if cost > dist[vert][id_zamku]:
            continue

        if vert == t:
            kwota_skradziona = V[id_zamku] if id_zamku != n else 0
            if result > dist[vert][id_zamku] - kwota_skradziona:
                result = dist[vert][id_zamku] - kwota_skradziona

            if kwota_skradziona == 0:
                if result > dist[vert][n] - V[vert]:
                    result = dist[vert][n] - V[vert]

        for child, child_cost in G[vert]:
            if id_zamku == n:
                if dist[child][n] > dist[vert][n] + child_cost:
                    dist[child][n] = dist[vert][n] + child_cost
                    pq.put((dist[vert][n] + child_cost, child, n))

                # moge teraz ukrasc to co jest w vert
                if dist[child][vert] > dist[vert][n] + 2 * child_cost + r:
                    dist[child][vert] = dist[vert][n] + 2 * child_cost + r
                    pq.put((dist[vert][n] + 2 * child_cost + r, child, vert))

            else:
                if dist[child][id_zamku] > dist[vert][id_zamku] + 2 * child_cost + r:
                    dist[child][id_zamku] = dist[vert][id_zamku] + 2 * child_cost + r
                    pq.put((dist[vert][id_zamku] + 2 * child_cost + r, child, id_zamku))

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)
