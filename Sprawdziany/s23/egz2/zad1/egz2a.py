from egz2atesty import runtests

"""
Złożoność najgorsza O(n^2)


def dominance(P: list[tuple[int, int]]) -> int:
    n = len(P)
    result = 0

    for i in range(n):
        x, y = P[i]
        points = 0
        for j in range(n):
            if i == j:
                continue

            if x > P[j][0] and y > P[j][1]:
                points += 1

        if points > result:
            result = points

    return result

"""
"""
Złożoność średnia O(nlogn)


def dominance(P: list[tuple[int, int]]) -> int:
    n = len(P)
    P.sort(key=lambda x: (x[1], x[0]))

    points = 0
    x, y = P[-1]

    for i in range(n - 2, -1, -1):
        if x > P[i][0] and y > P[i][1]:
            points += 1

    return points


"""
"""
Złożoność wzorcowa O(n)
"""


def dominance(P: list[tuple[int, int]]) -> int:
    n = len(P)
    if n == 0:
        return 0

    T = [0] * (n + 2)
    buckets = [[] for _ in range(n + 1)]

    for x, y in P:
        T[y] += 1
        buckets[x].append(y)

    for i in range(n, 0, -1):
        T[i] += T[i + 1]

    najwieksze_y = 0
    przetworzone_punkty = 0
    result = 0

    for x in range(n, 0, -1):
        col = buckets[x]
        if not col:
            continue

        current_najwiekszy = max(col)

        if current_najwiekszy > najwieksze_y:
            k = col.count(current_najwiekszy)

            punkty_po_lewej = n - (przetworzone_punkty + len(col))

            za_wysokie_po_lewej = T[current_najwiekszy] - k

            zdominowane = punkty_po_lewej - za_wysokie_po_lewej

            if zdominowane > result:
                result = zdominowane

            najwieksze_y = current_najwiekszy

        przetworzone_punkty += len(col)

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance, all_tests=True)
