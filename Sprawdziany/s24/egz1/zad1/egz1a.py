from egz1atesty import runtests
from queue import PriorityQueue


def armstrong(
    B: list[tuple[int, int, int]], G: list[tuple[int, int, int]], s: int, t: int
) -> int:
    n = 0
    for u, v, _ in G:
        n = max(u, v, n)
    n += 1  # znalezienie najwiekszego wierzcholka

    Rowery = [[] for _ in range(n)]
    NG = [[] for _ in range(n)]

    for u, v, w in G:
        NG[u].append((v, w))
        NG[v].append((u, w))

    for u, p, q in B:
        Rowery[u].append((p, q))

    dist = {}
    dist[(s, 1)] = 0

    pq = PriorityQueue()
    pq.put((0, s, 1))

    while not pq.empty():
        cost, vert, mnoznik = pq.get()

        if vert == t:
            return int(cost)

        # Odrzucamy stany, które są gorsze niż te zapisane w słowniku
        if cost > dist.get((vert, mnoznik), float("inf")):
            continue

        for child, child_cost in NG[vert]:
            # 1. Kontynuacja podróży w obecnym stanie (pieszo lub na tym samym rowerze)
            new_cost = cost + child_cost * mnoznik
            if new_cost < dist.get((child, mnoznik), float("inf")):
                dist[(child, mnoznik)] = new_cost
                pq.put((new_cost, child, mnoznik))

            # (możliwe tylko, jeśli dotarliśmy tutaj pieszo, czyli mnoznik == 1)
            if mnoznik == 1:
                for krotka in Rowery[vert]:
                    p, q = krotka[0], krotka[1]
                    nowy_mnoznik = p / q

                    new_cost_rower = cost + child_cost * nowy_mnoznik
                    if new_cost_rower < dist.get((child, nowy_mnoznik), float("inf")):
                        dist[(child, nowy_mnoznik)] = new_cost_rower
                        pq.put((new_cost_rower, child, nowy_mnoznik))

    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(armstrong, all_tests=True)
