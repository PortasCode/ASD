from random import randint
import heapq

ruchy_krola = [
    (-1, -1),
    (0, -1),
    (1, -1),  # Górny lewy, Góra, Górny prawy
    (-1, 0),
    (1, 0),  # Lewo,             Prawo
    (-1, 1),
    (0, 1),
    (1, 1),  # Dolny lewy, Dół,  Dolny prawy
]


def kings_path():
    global ruchy_krola

    N = int(input("N: "))
    Board = [[randint(1, 5) for _ in range(N)] for _ in range(N)]
    Board[0][0] = 0
    Q = []

    Results = [[float("inf") for _ in range(N)] for _ in range(N)]

    # koszt przejscia do tego pola, wspolrzedne x, wspolrzedne y
    Q = heapq.heappush(Q, (Board[0][0], 0, 0))
    Results[0][0] = 0

    while Q:
        koszt, x, y = heapq.heappop(Q)

        if koszt > Results[y][x]:
            continue

        for dx, dy in ruchy_krola:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N:
                nowy_koszt = koszt + Board[ny][nx]

                if nowy_koszt < Results[ny][nx]:
                    Results[ny][nx] = nowy_koszt
                    heapq.heappush(Q, (nowy_koszt, nx, ny))

    return Results[N - 1][N - 1]
