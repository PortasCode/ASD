# Czarny las   L - tablica drzew (jest to os i na wzor tej osi rosna drzewa, w tablicy jest dana wysokosc drzew)


def czarny_las(L: list[int]):
    n = len(L)
    T = [0 for _ in range(n)]

    if n == 0:
        return 0
    if n == 1:
        return L[0]

    T[0] = L[0]
    T[1] = max(L[0], L[1])

    for i in range(2, n):
        T[i] = max(T[i - 2] + L[i], T[i - 1])

    return T[n - 1]
