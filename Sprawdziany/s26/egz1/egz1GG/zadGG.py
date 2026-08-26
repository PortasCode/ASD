from zadGGtesty import runtests
from collections import deque

"""
Złożonośc akceptowalna O((E+V)V)

def bfs(G: list[list[int]], zbior: set[int], vert: int):
    n = len(G)
    visited = [False for _ in range(n)]
    Q = deque()
    Q.append(vert)
    visited[vert] = True

    while Q:
        u = Q.popleft()

        for v in G[u]:
            if not visited[v] and v in zbior:
                visited[v] = True
                Q.append(v)

    return visited


def game(G: list[list[int]], M: list[int], W: list[tuple[int, int, int]]):
    n = len(G)
    wykorzsytane_polaczenia = [0] * len(W)

    pierwsze_punkty_aleksander = True
    total_punkty_aleksander = 0
    pierwsze_punkty_barbara = True
    total_punkty_barbara = 0
    wierzcholki_aleksader = set()
    wierzcholki_barbara = set()

    for indeks, vert in enumerate(M):
        visited = []

        if indeks % 2 == 0:
            wierzcholki_aleksader.add(vert)
            visited = bfs(G, wierzcholki_aleksader, vert)
        else:
            wierzcholki_barbara.add(vert)
            visited = bfs(G, wierzcholki_barbara, vert)

        punkty = 0
        for idx, (a, b, points) in enumerate(W):
            if visited[a] and visited[b] and wykorzsytane_polaczenia[idx] == 0:
                punkty += points
                wykorzsytane_polaczenia[idx] = 1

        if indeks % 2 == 0:
            if pierwsze_punkty_aleksander and punkty > 0:
                pierwsze_punkty_aleksander = False
                punkty *= 2
            total_punkty_aleksander += punkty
        else:
            if pierwsze_punkty_barbara and punkty > 0:
                pierwsze_punkty_barbara = False
                punkty *= 2
            total_punkty_barbara += punkty

    return total_punkty_aleksander, total_punkty_barbara
"""


class FindUnion:
    def __init__(self, n: int):
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [0] * n

    def find(self, a: int) -> int:
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a: int, b: int):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.rank[a] > self.rank[b]:
            self.parent[b] = a
        else:
            self.parent[a] = b
            if self.rank[a] == self.rank[b]:
                self.rank[b] += 1


def game(G: list[list[int]], M: list[int], W: list[tuple[int, int, int]]):
    n = len(G)

    wierzcholki_aleksander = FindUnion(n)
    wierzcholki_barbara = FindUnion(n)

    punktowane_polaczenia = {}
    for u, v, p in W:
        punktowane_polaczenia[u] = (v, p)
        punktowane_polaczenia[v] = (u, p)

    # Pudełka na cele (zbiory) dla każdego wierzchołka
    cele_aleksander = [{i} if i in punktowane_polaczenia else set() for i in range(n)]
    cele_barbara = [{i} if i in punktowane_polaczenia else set() for i in range(n)]

    zajete_aleksander = [False] * n
    zajete_barbara = [False] * n

    aleksander_total_points = 0
    barbara_total_points = 0
    pierwsze_punkty_aleksander = True
    pierwsze_punkty_barbara = True

    for indeks, u in enumerate(M):
        tura_aleksandra = indeks % 2 == 0
        zdobyte_punkty_w_tej_turze = 0

        if tura_aleksandra:
            zajete_aleksander[u] = True
            aktualne_dsu = wierzcholki_aleksander
            aktualne_zajete = zajete_aleksander
            aktualne_cele = cele_aleksander
        else:
            zajete_barbara[u] = True
            aktualne_dsu = wierzcholki_barbara
            aktualne_zajete = zajete_barbara
            aktualne_cele = cele_barbara

        # Przeglądamy wszystkich sąsiadów nowo zajętego wierzchołka
        for v in G[u]:
            if aktualne_zajete[v]:
                szef_u = aktualne_dsu.find(u)
                szef_v = aktualne_dsu.find(v)

                # Jeśli łączymy dwie oddzielne grupy
                if szef_u != szef_v:
                    # Ustalamy, która grupa ma mniej celów w swoim pudełku
                    if len(aktualne_cele[szef_u]) < len(aktualne_cele[szef_v]):
                        maly_szef, duzy_szef = szef_u, szef_v
                    else:
                        maly_szef, duzy_szef = szef_v, szef_u

                    # Przesypujemy cele z mniejszego pudełka do większego
                    for cel in aktualne_cele[maly_szef]:
                        partner, punkty = punktowane_polaczenia[cel]

                        # Czy partner jest już zajęty przez tego gracza i należy do dużego pudełka?
                        if (
                            aktualne_zajete[partner]
                            and aktualne_dsu.find(partner) == duzy_szef
                        ):
                            zdobyte_punkty_w_tej_turze += punkty
                            # Usuwamy partnera, bo już nie musi czekać
                            aktualne_cele[duzy_szef].discard(partner)
                        else:
                            # Partnera jeszcze nie ma, więc wrzucamy cel do dużego pudełka
                            aktualne_cele[duzy_szef].add(cel)

                    # Czyścimy mniejsze pudełko, aby oszczędzić pamięć
                    aktualne_cele[maly_szef] = set()

                    # Łączymy grupy w samej strukturze DSU
                    aktualne_dsu.union(maly_szef, duzy_szef)

                    # Połączenie mogło zmienić głównego szefa (zgodnie z rank w DSU),
                    # upewniamy się, że nowy korzeń ma podpięte to zebrane duże pudełko
                    nowy_korzen = aktualne_dsu.find(maly_szef)
                    if nowy_korzen != duzy_szef:
                        aktualne_cele[nowy_korzen] = aktualne_cele[duzy_szef]

        # Podliczanie punktów i premie po zakończeniu ruchu
        if tura_aleksandra:
            if zdobyte_punkty_w_tej_turze > 0 and pierwsze_punkty_aleksander:
                pierwsze_punkty_aleksander = False
                zdobyte_punkty_w_tej_turze *= 2
            aleksander_total_points += zdobyte_punkty_w_tej_turze
        else:
            if zdobyte_punkty_w_tej_turze > 0 and pierwsze_punkty_barbara:
                pierwsze_punkty_barbara = False
                zdobyte_punkty_w_tej_turze *= 2
            barbara_total_points += zdobyte_punkty_w_tej_turze

    return aleksander_total_points, barbara_total_points


runtests(game, all_tests=True)
