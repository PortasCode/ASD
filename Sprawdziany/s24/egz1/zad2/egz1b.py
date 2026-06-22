from egz1btesty import runtests
from queue import PriorityQueue


def kstrong_n3logn(T, k):
    n = len(T)

    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            przedzial = T[i : j + 1]
            przedzial.sort()
            suma = sum(przedzial[k:])

            if suma > result:
                result = suma

    return result


def kstrong_n2logn(T, k):
    n = len(T)

    result = 0

    for i in range(n):
        suma = 0
        najgorsze_liczby = PriorityQueue()
        suma_do_usuniecia = 0
        licznik_najmniejszych = 0
        for j in range(i, n):
            suma += T[j]

            if T[j] < 0:
                najgorsze_liczby.put(-T[j])
                suma_do_usuniecia += T[j]
                licznik_najmniejszych += 1

                if licznik_najmniejszych > k:
                    juz_nie_najmniejsza = najgorsze_liczby.get()
                    licznik_najmniejszych -= 1
                    suma_do_usuniecia += juz_nie_najmniejsza

            if suma - suma_do_usuniecia > result:
                result = suma - suma_do_usuniecia

    return result


def kstrong_nk(T, k):
    n = len(T)

    dp = [[-float("inf") for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(k + 1):
            if j == 0:
                # albo powiekszamy albo ciag, albo zaczynamy nowy
                dp[i][j] = max(dp[i - 1][j] + T[i - 1], T[i - 1])
            else:
                # albo bierzemy, albo nie ale wtedy musimy sie cofnac o jedno usuniecie wstecz
                dp[i][j] = max(dp[i - 1][j] + T[i - 1], dp[i - 1][j - 1])

    return max(max(row) for row in dp)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kstrong_n2logn, all_tests=True)
