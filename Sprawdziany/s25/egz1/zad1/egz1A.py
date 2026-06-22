from egz1Atesty import runtests


""" 
Złożoność programu; O( (n+m)log(n+m) )

Sortuje po połączonej tablicy katapult i procesorów, co daje mi właśnie O(n+m)log(n+m)
Następnie mam pętle for o liczbe iteracji O(n+m), oraz w pętli for mam pętle while którą przetrzymuje dane dotyczące katapult.
Każda katapulta może wejść na stos i z niego zejść dokładnie 1 raz dlatego maksymalna liczba wykonań pętli while jest O(n) co daje nam

O( (n+m)log(n+m) + (2n + m) ) -> O( (n+m)log(n+m) )
"""


def battle_DP(P: list[int], K: list[int], R: list[int]) -> int:
    m = len(P)
    n = len(K)
    NK: list[tuple[int, int]] = []
    for indeks in range(n):
        temp = (K[indeks], R[indeks])
        NK.append(temp)

    P.sort()
    NK.sort()

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            wspolrzedne_procesora = P[j - 1]
            wspolrzedne_katapulty, zasieg_katapulty = tuple(NK[i - 1])

            if 0 < wspolrzedne_procesora - wspolrzedne_katapulty <= zasieg_katapulty:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

    return dp[n][m]


def battle(P: list[int], K: list[int], R: list[int]) -> int:
    T: list[tuple[int, int, str]] = []
    n = len(K)

    for indeks in range(n):
        krotka = (K[indeks], R[indeks], "k")
        T.append(krotka)

    for element in P:
        krotka = (element, -1, "p")
        T.append(krotka)

    T.sort(key=lambda x: x[0])

    stos = []
    result = 0
    for element in T:
        if element[2] == "k":
            stos.append(element)
            continue

        wspolrzedne_procesora = element[0]

        while len(stos) > 0:
            wspolrzedne_katapulty, zasieg_katapulty, _ = stos.pop()
            if wspolrzedne_procesora - wspolrzedne_katapulty <= zasieg_katapulty:
                result += 1
                break

    return result


def countingsort(A, m):
    n = len(A)
    B = [(0, 0, 0)] * n
    C = [0] * (m + 1)

    for i in range(n):
        C[A[i][0]] += 1

    for i in range(1, m + 1):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[A[i][0]] -= 1
        B[C[A[i][0]]] = A[i]

    return B


def battle_wzorcowa(P: list[int], K: list[int], R: list[int]) -> int:
    NT = []
    n = len(K)
    m = len(P)

    for element in P:
        NT.append((element, -1, "p"))

    for i in range(n):
        NT.append((K[i], R[i], "k"))

    najwieksza_wartosc = max(element[0] for element in NT)

    NT = countingsort(NT, najwieksza_wartosc)
    stos = []
    result = 0
    for krotka in NT:
        if krotka[2] == "k":
            stos.append(krotka)
            continue

        while len(stos) > 0:
            wspolrzedne_katapulty, zasieg_katapulty, _ = stos.pop()
            if krotka[0] - wspolrzedne_katapulty <= zasieg_katapulty:
                result += 1
                break

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(battle_wzorcowa, all_tests=True)
