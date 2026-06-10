def wybor_zadan_z_terminami(T: set[int], D: list[int], G: list[int]) -> int:
    A = []
    for element in T:
        krotka = (G[element], D[element])
        A.append(krotka)

    maksymalny_termin = max(D)
    terminy = [0] * (maksymalny_termin + 1)
    A.sort(key=lambda x: x[0], reverse=True)

    for zysk, termin in A:
        for indeks in range(termin, 0, -1):
            if terminy[indeks] == 0:
                terminy[indeks] = zysk
                break

    return sum(terminy)
