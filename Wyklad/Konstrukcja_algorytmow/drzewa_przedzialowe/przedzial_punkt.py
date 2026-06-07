import math


class DrzewoPrzedzialPunkt:
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

    def dodaj_na_przedziale(self, poczatek, koniec, wartosc):
        a = self.base + poczatek
        b = self.base + koniec

        if a == b:
            self.drzewo[a] += wartosc
            return

        a -= 1
        b += 1

        while b - a > 1:
            if a % 2 == 0:
                self.drzewo[a + 1] += wartosc
            if b % 2 == 1:
                self.drzewo[b - 1] += wartosc

            a //= 2
            b //= 2

    def zapytaj_o_punkt(self, indeks):
        v = self.base + indeks
        wynik = 0

        while v > 0:
            wynik += self.drzewo[v]
            v //= 2

        return wynik


dane = [0, 0, 0, 0, 0, 0]

drzewo = DrzewoPrzedzialPunkt(dane)

drzewo.dodaj_na_przedziale(1, 4, 10)

drzewo.dodaj_na_przedziale(3, 5, 5)

print("Wartość na indeksie 0 (poza przedziałami):", drzewo.zapytaj_o_punkt(0))
print(
    "Wartość na indeksie 2 (załapał się tylko na pierwsze dodawanie):",
    drzewo.zapytaj_o_punkt(2),
)
print(
    "Wartość na indeksie 4 (załapał się na oba dodawania):", drzewo.zapytaj_o_punkt(4)
)
