def minimalne_tankowanie(B: int, L: int, T: list[int]) -> int:
    result = 0
    i = 0
    n = len(T)
    position = 0

    while position + L < B:
        najdalsza_stacja = position

        while i < n and T[i] <= position + L:
            najdalsza_stacja = T[i]
            i += 1

        if najdalsza_stacja == position:
            return -1

        position = najdalsza_stacja
        result += 1

    return result


def minimalne_tankowanie_v2(B: int, L: int, T: list[int], C: list[float]) -> float:
    T.append(B)
    C.append(0.0)
    n = len(T)
    i = 0
    total_cost = 0.0
    obecne_paliwo = L

    while i < n - 1:
        if T[i + 1] - T[i] > L:
            return -1.0

        nastepna_stacja = -1
        najtansza_w_zasiegu = -1
        min_cena = float("inf")

        for j in range(i + 1, n):
            odleglosc = T[j] - T[i]
            if odleglosc > L:
                break

            if C[j] <= C[i]:
                nastepna_stacja = j
                break

            if C[j] < min_cena:
                min_cena = C[j]
                najtansza_w_zasiegu = j

        if nastepna_stacja != -1:
            potrzebne_paliwo = T[nastepna_stacja] - T[i]

            if obecne_paliwo < potrzebne_paliwo:
                total_cost += (potrzebne_paliwo - obecne_paliwo) * C[i]
                obecne_paliwo = potrzebne_paliwo

            obecne_paliwo -= potrzebne_paliwo
            i = nastepna_stacja

        else:
            total_cost += (L - obecne_paliwo) * C[i]
            obecne_paliwo = L - (T[najtansza_w_zasiegu] - T[i])
            i = najtansza_w_zasiegu

    return total_cost
