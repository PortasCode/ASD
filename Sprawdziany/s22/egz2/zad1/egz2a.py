from egz2atesty import runtests
import math


def coal(A: list[int], T: int):
    n = len(A)
    M = [0] * n

    ostatni_indeks = -1
    for transport in A:
        for i in range(n):
            if M[i] + transport <= T:
                ostatni_indeks = i
                M[i] += transport
                break
    return ostatni_indeks


class Drzewo:
    def __init__(self, rozmiar, T):
        potega = math.ceil(math.log2(rozmiar)) if rozmiar > 1 else 0
        self.base = 2**potega
        self.drzewo = [T] * (2 * self.base)

    def aktualizacja(self, wartosc):
        v = 1

        while v < self.base:
            if self.drzewo[2 * v] >= wartosc:
                v = 2 * v
            else:
                v = 2 * v + 1

        result = v - self.base
        self.drzewo[v] -= wartosc

        v //= 2

        while v > 1:
            self.drzewo[v] = max(self.drzewo[2 * v], self.drzewo[2 * v + 1])
            v //= 2

        return result


def coal_nlogn(A: list[int], T: int):
    n = len(A)
    tree = Drzewo(n, T)

    last_indeks = -1
    for i in range(n):
        last_indeks = tree.aktualizacja(A[i])

    return last_indeks


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(coal, all_tests=True)
