from collections import deque


# spraedzanie czy podany graf jest dwódzielny
def czy_dwudzielny(G: list[list[int]]) -> bool:
    n = len(G)
    kolorowanie = [-1 for _ in range(n)]
    Q = deque()
    for i in range(n):
        if kolorowanie[i] == -1:
            Q.append(i)
            kolorowanie[i] = 0

        while Q:
            u = Q.popleft()
            for v in G[u]:
                if kolorowanie[v] == -1:
                    kolorowanie[v] = (kolorowanie[u] + 1) % 2
                    Q.append(v)
                else:
                    if kolorowanie[u] == kolorowanie[v]:
                        return False
    return True


# zliczenie ile jest spojnych skladowych w grafie
def ile_spojnych_skladow_w_grafie(G: list[list[int]]):
    n = len(G)
    visited = [False for _ in range(n)]
    result = []

    def DFS(u: int):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                DFS(v)
        result.append(u)

    licznik = 0
    for i in range(n):
        if not visited[i]:
            licznik += 1
            DFS(i)

    return licznik
