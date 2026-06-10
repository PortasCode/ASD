def pokrycie_przedzialami_jednostkowymi(X: set[float]) -> int:
    T = list(X)
    T.sort()
    n = len(T)
    if n == 0:
        return 0

    if n == 1:
        return 1

    indeks = 1
    ostatni = T[0]
    result = 1
    while indeks < n:
        if T[indeks] - ostatni > 1:
            result += 1
            ostatni = T[indeks]
        indeks += 1

    return result
