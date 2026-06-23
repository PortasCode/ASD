from egz3btesty import runtests


def uncool(P: list[tuple[int, int]]):
    n = len(P)
    T = []
    for i in range(n):
        T.append((P[i][0], P[i][1], i))

    T.sort(key=lambda x: (x[0], -x[1]))

    y_max = T[0][1]
    x_max = T[0][0]
    indeks = T[0][2]
    for i in range(1, n):
        x, y, og = T[i]
        if x >= x_max and y <= y_max:
            continue
        elif x > y_max:
            indeks = og
            x_max = x
            y_max = y
        else:
            return (indeks, og)

    # tu prosze wpisac wlasna implementacje
    pass


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(uncool, all_tests=True)
