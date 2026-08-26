from egz2btesty import runtests
from queue import PriorityQueue
from collections import deque


"""
Złożoność średnia O(mlogm)
def tory_amos(E: list[tuple[int, int, int, str]], A: int, B: int):
    n = 0
    for u, v, _, _ in E:
        n = max(n, u, v)
    n += 1

    G = [[] for _ in range(n)]
    for u, v, d, t in E:
        nt = t == "I"
        G[u].append((v, d, nt))
        G[v].append((u, d, nt))

    pq = PriorityQueue()
    dist = [[float("inf"), float("inf")] for _ in range(n)]
    dist[A] = [0, 0]

    for v, d, t in G[A]:
        pq.put((d, v, t))

    while not pq.empty():
        cost, vert, rail = pq.get()

        if cost > dist[vert][rail]:
            continue

        if vert == B:
            return cost

        for child, child_cost, child_rail in G[vert]:
            total_cost = cost + child_cost
            if child_rail == rail:
                if rail == 0:
                    total_cost += 10
                else:
                    total_cost += 5
            else:
                total_cost += 20

            if total_cost < dist[child][child_rail]:
                dist[child][child_rail] = total_cost
                pq.put((total_cost, child, child_rail))

    return -1
"""

"""
Złożoność wzorcowa O(m)


def tory_amos(E: list[tuple[int, int, int, str]], A: int, B: int):
    n = 0
    for u, v, _, _ in E:
        n = max(n, u, v)
    n += 1

    G = [[] for _ in range(n)]
    for u, v, d, t in E:
        nt = t == "I"
        G[u].append((v, d, nt))
        G[v].append((u, d, nt))

    Q = deque()
    dist = [[float("inf"), float("inf")] for _ in range(n)]
    dist[A] = [0, 0]

    for v, d, t in G[A]:
        Q.append((d, v, t))

    while Q:
        cost, vert, rail = Q.popleft()

        if cost > dist[vert][rail]:
            continue

        if vert == B:
            continue

        for child, child_cost, child_rail in G[vert]:
            total_cost = cost + child_cost
            if child_rail == rail:
                if rail == 0:
                    total_cost += 10
                else:
                    total_cost += 5
                if total_cost < dist[child][child_rail]:
                    dist[child][child_rail] = total_cost
                    Q.appendleft((total_cost, child, child_rail))
            else:
                total_cost += 20
                if total_cost < dist[child][child_rail]:
                    dist[child][child_rail] = total_cost
                    Q.append((total_cost, child, child_rail))

    return min(dist[B])

"""
"""
Algorytm Diala O(m)
"""


def tory_amos(E: list[tuple[int, int, int, str]], A: int, B: int):
    if A == B:
        return 0

    n = 0
    for u, v, _, _ in E:
        n = max(n, u, v)
    n += 1

    G = [[] for _ in range(n)]
    for u, v, d, t in E:
        nt = 1 if t == "I" else 0
        G[u].append((v, d, nt))
        G[v].append((u, d, nt))

    K = 31
    buckets = [[] for _ in range(K)]
    elements_in_buckets = 0

    dist = [[float("inf"), float("inf")] for _ in range(n)]
    dist[A] = [0, 0]

    for v, d, t in G[A]:
        if d < dist[v][t]:
            dist[v][t] = d
            buckets[d % K].append((d, v, t))
            elements_in_buckets += 1

    curr_cost = 0

    while elements_in_buckets > 0:
        bucket_idx = curr_cost % K

        while not buckets[bucket_idx]:
            curr_cost += 1
            bucket_idx = curr_cost % K

        while buckets[bucket_idx]:
            cost, vert, rail = buckets[bucket_idx].pop()
            elements_in_buckets -= 1

            if cost > dist[vert][rail]:
                continue

            if vert == B:
                continue

            for child, child_cost, child_rail in G[vert]:
                total_cost = cost + child_cost

                if child_rail == rail:
                    if rail == 0:
                        total_cost += 10
                    else:
                        total_cost += 5
                else:
                    total_cost += 20

                if total_cost < dist[child][child_rail]:
                    dist[child][child_rail] = total_cost
                    buckets[total_cost % K].append((total_cost, child, child_rail))
                    elements_in_buckets += 1

    ans = min(dist[B])
    return ans if ans != float("inf") else -1


runtests(tory_amos, all_tests=True)
