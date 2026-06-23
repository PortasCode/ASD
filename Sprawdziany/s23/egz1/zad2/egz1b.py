from egz1btesty import runtests


def planets(D: list[int], C: list[int], T: list[tuple[int, int]], E: int):
    n = len(D)

    dp = [[float("inf") for _ in range(E + 1)] for _ in range(n)]
    for e in range(E + 1):
        dp[0][e] = e * C[0]

    if T[0][0] != 0:
        dp[T[0][0]][0] = min(dp[T[0][0]][0], T[0][1])

    for i in range(1, n):
        for j in range(E + 1):
            # opcja przylecenia tutaj
            trasa = D[i] - D[i - 1]
            koszt_przylotu = float("inf")
            if j + trasa <= E:
                koszt_przylotu = dp[i - 1][j + trasa]

            # lepiej do tej ilosci paliwa dotankowac
            koszt_dotankoawnia = float("inf")
            if j != 0:
                koszt_dotankoawnia = dp[i][j - 1] + C[i]

            dp[i][j] = min(dp[i][j], koszt_dotankoawnia, koszt_przylotu)

            if j == 0:
                kierunek_poratlu, cena_biletu = T[i]
                if kierunek_poratlu != i:
                    dp[kierunek_poratlu][0] = min(
                        dp[kierunek_poratlu][0], dp[i][0] + cena_biletu
                    )
    return min(dp[n - 1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
