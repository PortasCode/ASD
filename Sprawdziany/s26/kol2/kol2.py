from kol2_test import runtests
from queue import PriorityQueue
from collections import deque

"""
Złożoność podstawowa O(m^2)

def change(mosty: list[tuple[int, int, str]], poczty: list[int], s: int):
    return 0

"""


def zmien_czapke_na_int(czapka: str) -> int:
    return int(czapka == "B")


"""
Złożoność średnia O(mlogm)


def change(mosty: list[tuple[int, int, str]], poczty: list[int], s: int) -> int:
    n = 0
    for u, v, _ in mosty:
        n = max(n, u, v)
    n += 1

    G = [[] for _ in range(n)]

    for u, v, czapka in mosty:
        typ = zmien_czapke_na_int(czapka)
        G[u].append((v, typ))
        G[v].append((u, typ))

    zbior_poczty = set(poczty)

    dist = [[float("inf"), float("inf")] for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0, s, -1))
    result = n + 1

    while not pq.empty():
        liczba_zmian, vert, aktualna_czapka = pq.get()

        if vert in zbior_poczty:
            result = liczba_zmian
            break

        if aktualna_czapka == -1:
            for child, przyszla_czapka in G[vert]:
                dist[child][przyszla_czapka] = 0
                pq.put((0, child, przyszla_czapka))

        if liczba_zmian > dist[vert][aktualna_czapka]:
            continue

        for child, przyszla_czapka in G[vert]:
            if przyszla_czapka == aktualna_czapka:
                if liczba_zmian < dist[child][aktualna_czapka]:
                    dist[child][aktualna_czapka] = liczba_zmian
                    pq.put((liczba_zmian, child, aktualna_czapka))

            else:
                if liczba_zmian + 1 < dist[child][przyszla_czapka]:
                    dist[child][przyszla_czapka] = liczba_zmian + 1
                    pq.put((liczba_zmian + 1, child, przyszla_czapka))

    return result

"""

"""
Złożoność wzorcowa O(m)
"""


def change(mosty: list[tuple[int, int, str]], poczty: list[int], s: int) -> int:
    n = 0
    for u, v, _ in mosty:
        n = max(n, u, v)
    n += 1

    G = [[] for _ in range(n)]
    for u, v, czapka in mosty:
        typ = zmien_czapke_na_int(czapka)
        G[u].append((v, typ))
        G[v].append((u, typ))

    zbior_poczty = set(poczty)

    dist = [[float("inf"), float("inf")] for _ in range(n)]
    Q = deque()

    if s in zbior_poczty:
        return 0

    for child, typ_czapki in G[s]:
        if dist[child][typ_czapki] == float("inf"):
            dist[child][typ_czapki] = 0
            Q.appendleft((0, child, typ_czapki))

    while Q:
        liczba_zmian, vert, aktualna_czapka = Q.popleft()

        if liczba_zmian > dist[vert][aktualna_czapka]:
            continue

        if vert in zbior_poczty:
            return liczba_zmian

        for child, przyszla_czapka in G[vert]:
            koszt_przejscia = 0 if przyszla_czapka == aktualna_czapka else 1
            nowy_koszt = liczba_zmian + koszt_przejscia

            if nowy_koszt < dist[child][przyszla_czapka]:
                dist[child][przyszla_czapka] = nowy_koszt

                if koszt_przejscia == 0:
                    Q.appendleft((nowy_koszt, child, przyszla_czapka))
                else:
                    Q.append((nowy_koszt, child, przyszla_czapka))

    return -1


runtests(change, all_tests=True)
