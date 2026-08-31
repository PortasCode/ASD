"""
432101 Mateusz Portka

Złożoność obliczeniowa algorytmu: O(E^2 + VE)
Złożoność pamięciowa algorytmu: O(V+E)

Opis działania algorytmu:
    1) Dwukrotnie przechodzę po tablicy G aby móc stworzyć Graph który będzie grfem G ale w formacie listy sąsiedztwa - O(E)
    2) Wywouje funkcję find_bridges, która zwraca mi listę krotek (list[tuple[int,int]]) wszysktich mostów w tym grafie - O(V+E)
    3) Dla każdego mostu w grafie G - O(E)
        4) Usuwam wskazaną krawędź (most) z grafu G - O(1)
        5) Funkcja Dfs zwraca mi tablicę visited (wierzchołki należące do jednego obszaru królestwa ) - O(V+E)
        6) Obliczam liczbe wierzchołków w tym obszarze - O(V)
        7) Obliczam liczbe wierzchołków w drugim obszarze oraz uaktualniam wynik jeżeli abs(U-V) < wynik - O(1)
        8) Dodaję z powrotem wskazaną krawędź do grafu G - O(1)
    9) Zwracam wynik - O(1)

Obliczenia złożoności:
O(2E + V + E(2V+E)) -> O(V + E + E^2 + VE) -> O(E^2 + VE)
"""

from zadPKtesty import runtests


def find_bridges(G: list[set[int]]):
    n = len(G)
    curr_time = 0

    time_in = [0 for _ in range(n)]
    low = [0 for _ in range(n)]
    bridges = []

    def dfs(vert, parent):
        nonlocal curr_time

        curr_time += 1
        time_in[vert] = low[vert] = curr_time

        for child in G[vert]:
            if child == parent:
                continue
            if time_in[child] == 0:
                dfs(child, vert)
                low[vert] = min(low[vert], low[child])

                if low[child] == time_in[child]:
                    bridges.append((vert, child))
            else:
                low[vert] = min(low[vert], time_in[child])

    for vert in range(n):
        if time_in[vert] == 0:
            dfs(vert, -1)

    return bridges


def Dfs(G, start):
    n = len(G)
    visited = [False for _ in range(n)]

    def dfs(vert):
        visited[vert] = True

        for child in G[vert]:
            if not visited[child]:
                dfs(child)

    dfs(start)

    return visited


def partition(G: list[tuple[int, int]]):
    najwiekszy_wierzcholek = -1

    for u, v in G:
        najwiekszy_wierzcholek = max(najwiekszy_wierzcholek, u, v)

    n = najwiekszy_wierzcholek + 1
    Graph: list[set[int]] = [set() for _ in range(n)]

    for u, v in G:
        Graph[u].add(v)
        Graph[v].add(u)

    mosty = find_bridges(Graph)

    if len(mosty) == 0:
        return -1

    result = float("inf")

    for u, v in mosty:
        Graph[u].remove(v)
        Graph[v].remove(u)

        visited = Dfs(Graph, u)
        U = 0
        for i in range(n):
            if visited[i]:
                U += 1
        V = n - U

        if abs(U - V) < result:
            result = abs(U - V)

        Graph[u].add(v)
        Graph[v].add(u)

    if result == float("inf"):
        return -1

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(partition, all_tests=True)
