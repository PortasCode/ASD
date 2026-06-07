from queue import PriorityQueue


class PQ:
    def __init__(self):
        self.min_heap: list[tuple[int, int]] = []

    def __left(self, x: int):
        return 2 * x + 1

    def __right(self, x: int):
        return 2 * x + 2

    def __parent(self, x: int):
        return (x - 1) // 2

    def __heapify(self, i: int, n: int):
        min_ind = i
        li = self.__left(i)
        ri = self.__right(i)

        if li < n and self.min_heap[li] < self.min_heap[min_ind]:
            min_ind = li
        if ri < n and self.min_heap[ri] < self.min_heap[min_ind]:
            min_ind = ri

        if min_ind != i:
            self.min_heap[min_ind], self.min_heap[i] = (
                self.min_heap[i],
                self.min_heap[min_ind],
            )
            self.__heapify(min_ind, n)

    def size(self):
        return len(self.min_heap)

    def __bool__(self):
        return self.size() > 0

    def pop(self) -> tuple[int, int]:
        if self.size() == 1:
            return self.min_heap.pop()

        ret = self.min_heap[0]
        self.min_heap[0] = self.min_heap.pop()

        self.__heapify(0, self.size())
        return ret

    def insert(self, el: tuple[int, int]):
        self.min_heap.append(el)
        curr_ind = self.size() - 1
        while curr_ind > 0:
            par = self.__parent(curr_ind)
            if self.min_heap[par] > self.min_heap[curr_ind]:
                self.min_heap[par], self.min_heap[curr_ind] = (
                    self.min_heap[curr_ind],
                    self.min_heap[par],
                )
                curr_ind = par
            else:
                break


# lista sasiedztwa
# O(E log V)
def dijkstra(
    G: list[list[tuple[int, int]]], start: int
) -> tuple[list[float], list[int]]:
    n = len(G)

    parent: list[int] = [-1 for _ in range(n)]
    dist: list[float] = [float("inf") for _ in range(n)]

    pq: PriorityQueue[tuple[int, int]] = PriorityQueue()

    pq.put((0, start))
    dist[start] = 0

    while not pq.empty():
        cost, vert = pq.get()

        if cost > dist[vert]:
            continue

        for child, child_cost in G[vert]:
            if cost + child_cost < dist[child]:
                dist[child] = cost + child_cost
                parent[child] = vert
                pq.put((cost + child_cost, child))

    return dist, parent


# graf w reprezentacji macierzowej gdzie G[v][u] = -1 oznacza brak krawedzi
# O(V^2)
def dijkstra_matrix(G: list[list[int]], start: int):
    n = len(G)
    vis = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]

    dist[start] = 0
    for _ in range(n):
        min_dist = float("inf")
        vert = -1
        for u in range(n):
            if not vis[u] and dist[u] < min_dist:
                min_dist = dist[u]
                vert = u

        if vert == -1:
            break

        vis[vert] = True
        for child in range(n):
            w = G[vert][child]
            if w != -1 and not vis[child]:
                if dist[vert] + w < dist[child]:
                    dist[child] = dist[vert] + w
                    parent[child] = vert
    return dist, parent
