from egz2atesty import runtests


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


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(coal, all_tests=True)
