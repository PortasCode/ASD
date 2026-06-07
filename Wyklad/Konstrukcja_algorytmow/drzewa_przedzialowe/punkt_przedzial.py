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

    def aktualizuj(self, indeks, wartosc):
        v = self.base + indeks
        self.drzewo[v] = wartosc

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


dane = [2, 4, 1, 5, 3, 8]

drzewo = DrzewoPunktPrzedzial(dane)

print("Suma przed zmianą:", drzewo.suma_na_przedziale(1, 4))

drzewo.aktualizuj(2, 10)

print("Suma po zmianie:", drzewo.suma_na_przedziale(1, 4))
