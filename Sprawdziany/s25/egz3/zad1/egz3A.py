from egz3Atesty import runtests

"""
Złożoność podstawowa O(n^2)

def treecut(H: list[int], k: int):
    n = len(H)
    tablica = [0] * n

    for i in range(1, n):
        licznik = 0
        for j in range(0, i):
            if H[j] > H[i]:
                licznik += 1
        tablica[i] = tablica[i - 1] + licznik

    for i in range(1, n):
        if tablica[i] > k:
            return i
    return n

"""

"""
Złożoność średnia O(nlog^2n)

def merge(A, B, p, q, r):
    inwersje = 0
    i = p
    k = p
    j = q

    while i < q and j < r:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
            inwersje += q - i
        k += 1

    while i < q:
        B[k] = A[i]
        i += 1
        k += 1

    while j < r:
        B[k] = A[j]
        j += 1
        k += 1

    for i in range(p, r):
        A[i] = B[i]

    return inwersje


def mergesort(A, B, p, r):
    inwersje = 0
    if r - p > 1:
        q = (r + p) // 2
        inwersje += mergesort(A, B, p, q)
        inwersje += mergesort(A, B, q, r)
        inwersje += merge(A, B, p, q, r)
    return inwersje


def msort(A):
    n = len(A)
    B = [0] * n
    return mergesort(A, B, 0, n)


def treecut(H: list[int], k: int):
    n = len(H)
    left = 0
    right = n
    result = 1

    while left <= right:
        mid = (left + right) // 2
        inwersje = msort(H[:mid])

        if inwersje > k:
            right = mid - 1
        else:
            result = mid
            left = mid + 1

    return result
"""


# Złożoność najlepsza O(nlogn)


class DrzewoFennwcika:
    def __init__(self, n):
        self.bit = [0] * (n + 1)
        self.n = n

    def update(self, i):
        while i <= self.n:
            self.bit[i] += 1
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s


def binary_search(T, number):
    n = len(T)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if T[mid] == number:
            return mid

        if T[mid] > number:
            right = mid - 1
        else:
            left = mid + 1
    return right


def treecut(H: list[int], k: int):
    n = len(H)
    T = H.copy()
    T.sort()
    drzewo = DrzewoFennwcika(n)

    liczba_drzew = 0
    liczba_inwersji = 0
    for number in H:
        indeks_drzewa = binary_search(T, number) + 1
        # koryguje +1 bo w drzewie Fennwicka indeksujemy od 1

        temp = drzewo.query(indeks_drzewa)
        nowe_inwersje = liczba_drzew - temp
        if liczba_inwersji + nowe_inwersje > k:
            return liczba_drzew
        else:
            drzewo.update(indeks_drzewa)
            liczba_inwersji += nowe_inwersje
            liczba_drzew += 1

    return liczba_drzew


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(treecut, all_tests=True)
