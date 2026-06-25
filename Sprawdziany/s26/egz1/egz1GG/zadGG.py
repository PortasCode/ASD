"""
Mateusz Portka 432101

Złożoność alogrytmu O( (E+V)V )

Wyjaśnienie algorytmu:

1) Przechodzę po każdym wybranym wierzchołku w tablicy M

    2) Zaznaczam w tablicy wybrane_wierzcholki do kogo nalezy konkretny wierzcholek  O(1)

    3) Sprawdzam czy ten wierzcholek vert nie nalezy do jakiejs punktowanej trasy
    oraz nie byl wczesniej dodany juz do mozliwych tras Aleksandra lub Barbary O( 1/2 V )

    4) Uruchamiam BFS dla vert zeby sprwadzic do jakich wierzcholkow trasa jest mozliwa tylko dla konkretnego uczestnika O( V+E )

    5) Sprawdzam czy ktoras trasa jest mozliwa, jezeli tak to dodaje ją do uzytych tras, dodaje punkty oraz sprawdzam czy to sa
    pierwsze punkty danego uczestnika, pozniej dodaje do koncowego rezultatu O( 1/2 V )


O ( V * ( 1/2V + V + E + 1/2V ) )  --> O ( (E+V)V)

"""

from zadGGtesty import runtests
from collections import deque


def game(G: list[list[int]], M: list[int], W: list[tuple[int, int, int]]):
    n = len(G)
    punkty_A = 0
    punkty_B = 0

    mozliwe_trasy_A = set()
    uzyte_trasy_A = set()
    mozliwe_trasy_B = set()
    uzyte_trasy_B = set()

    # 0 - Alek          1 - Basia
    wybrane_wierzcholki = [-1 for _ in range(n)]

    dlugosc_M = len(M)
    for indeks in range(dlugosc_M):
        vert = M[indeks]

        if indeks % 2 == 0:
            flaga = False
            wybrane_wierzcholki[vert] = 0
        else:
            flaga = True
            wybrane_wierzcholki[vert] = 1

        # O( 1/2 V )
        for u, v, s in W:
            if (u, v, s) in mozliwe_trasy_A or (u, v, s) in mozliwe_trasy_B:
                continue
            if u == vert or v == vert:
                if flaga:
                    mozliwe_trasy_B.add((u, v, s))
                else:
                    mozliwe_trasy_A.add((u, v, s))

        # O( V + E )
        visited = [False for _ in range(n)]
        Q = deque()
        Q.append(vert)
        visited[vert] = True

        while len(Q) > 0:
            u = Q.popleft()

            for v in G[u]:
                if not visited[v] and wybrane_wierzcholki[v] == int(flaga):
                    visited[v] = True
                    Q.append(v)

        aktualne_punkty = 0

        # O( 1/2 V )
        if flaga:
            for trasa in mozliwe_trasy_B:
                if (
                    visited[trasa[0]]
                    and visited[trasa[1]]
                    and trasa not in uzyte_trasy_B
                ):
                    aktualne_punkty += trasa[2]
                    uzyte_trasy_B.add(trasa)

            if punkty_B == 0:
                punkty_B += 2 * aktualne_punkty
            else:
                punkty_B += aktualne_punkty

        else:
            for trasa in mozliwe_trasy_A:
                if (
                    visited[trasa[0]]
                    and visited[trasa[1]]
                    and trasa not in uzyte_trasy_A
                ):
                    aktualne_punkty += trasa[2]
                    uzyte_trasy_A.add(trasa)

            if punkty_A == 0:
                punkty_A += 2 * aktualne_punkty
            else:
                punkty_A += aktualne_punkty

    return (punkty_A, punkty_B)


runtests(game, all_tests=True)
