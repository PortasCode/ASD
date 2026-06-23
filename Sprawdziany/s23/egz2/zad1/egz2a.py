from egz2atesty import runtests
import math


class DrzewoPunktPrzedzial:
    def __init__(self, tablica):
        n = len(tablica)
        if n == 0:
            self.base = 0
            self.drzewo = []
            return

        potega = math.ceil(math.log2(n)) if n > 1 else 0
        self.base = 2**potega

        self.drzewo = [0] * (2 * self.base)

        for i in range(n):
            self.drzewo[self.base + i] = tablica[i]

        for i in range(self.base - 1, 0, -1):
            self.drzewo[i] = self.drzewo[i * 2] + self.drzewo[i * 2 + 1]

    def aktualizuj(self, indeks):
        v = self.base + indeks
        self.drzewo[v] += 1

        v //= 2
        while v > 0:
            self.drzewo[v] = self.drzewo[v * 2] + self.drzewo[v * 2 + 1]
            v //= 2

    def suma_na_przedziale(self, poczatek, koniec):
        a = self.base + poczatek
        b = self.base + koniec

        if a == b:
            return self.drzewo[a]

        wynik = 0

        a -= 1
        b += 1

        while b - a > 1:
            if a % 2 == 0:
                wynik += self.drzewo[a + 1]

            if b % 2 == 1:
                wynik += self.drzewo[b - 1]

            a //= 2
            b //= 2

        return wynik


def dominance_nlogn(P: list[tuple[int, int]]):
    n = len(P)
    P.sort(key=lambda x: (x[0], -x[1]))
    dane_y = [0] * (n + 1)

    drzewo = DrzewoPunktPrzedzial(dane_y)

    result = 0
    for i in range(n):
        if i == 0:
            drzewo.aktualizuj(P[i][1])
            continue

        liczba = drzewo.suma_na_przedziale(0, P[i][1] - 1)
        if liczba > result:
            result = liczba

        drzewo.aktualizuj(P[i][1])

    return result


def dominance_n(P: list[tuple[int, int]]):
    n = len(P)
    pogrupowane_punkty = [[] for _ in range(n + 1)]

    for krotka in P:
        pogrupowane_punkty[krotka[0]].append(krotka)

    L = [0 for _ in range(n + 1)]
    T = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        L[i] = L[i - 1] + len(pogrupowane_punkty[i - 1])

    zliczenia_y = [0 for _ in range(n + 1)]
    for x, y in P:
        zliczenia_y[y] += 1

    T = [0 for _ in range(n + 1)]
    T[n] = zliczenia_y[n]

    for i in range(n - 1, -1, -1):
        T[i] = T[i + 1] + zliczenia_y[i]

    najlepszy_wynik = 0
    najwiekszy_y_po_prawej = 0

    for x in range(n, -1, -1):
        if not pogrupowane_punkty[x]:
            continue

        current_max_y = -1
        liczba_kopii = 0

        for _, y in pogrupowane_punkty[x]:
            if y > current_max_y:
                current_max_y = y
                liczba_kopii = 1
            elif y == current_max_y:
                liczba_kopii += 1

        if current_max_y > najwiekszy_y_po_prawej:
            najwiekszy_y_po_prawej = current_max_y

            force = L[x] - T[current_max_y] + liczba_kopii

            if force > najlepszy_wynik:
                najlepszy_wynik = force

    return najlepszy_wynik


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance_n, all_tests=True)
