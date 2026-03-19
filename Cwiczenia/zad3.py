"""
ociepka@agh.edu.pl

1) Quicksort
max O(logn) pamieci

2) Znalezienie w nieposorotwanej tablicy
k-ty co do wielkosci w O(n)

3) Pojemnik na wodę
jest duzo pojemnikow o roznych ksztaltach, wszystkie pojemniki sa polaczone rurami oraz kazdy pojemnik ma jakies wspolrzedne na osi OY
dzieki temu wiemy na jakesj sa okolo wysokosci
nalewamy k litrow wody i interesuje nas ile pojemniokow bedzie w pelni napelnionych

4) Posortuj A[n] malejąco,
log(n) unikalnych wartosci
w zlozonosci O(nlog(logn))git pu
"""


# 1)
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    return i


def qsort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        if q - p < r - q:
            qsort(A, p, q - 1)
            qsort(A, q + 1, r)
        else:
            qsort(A, q + 1, r)
            qsort(A, p, q - 1)


# 2)
# zakladamy ze istnieje k-ty element istnieje, dane sa prawidlowe
def find_k_ty(A, p, r, k):
    if p < r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            return find_k_ty(A, q + 1, r, k)
        else:
            return find_k_ty(A, p, q - 1, k)
    return

# 3)
# Metoda 1
# nie interesuje nas wysokosc teg wszystkiego
# do zaimplementowania w domu


# Metoda 2
# binsearch, sprawdzamy ile wody jest potrzebne aby do tego poziomu ktory znalezlismy 
