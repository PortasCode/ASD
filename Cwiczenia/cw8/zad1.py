# Wydawanie monet  A - tablica nominałow   T - kwota do wydania


def wydawanie_monet(A: list[int], amount: int):
    T = [float("inf") for _ in range(amount + 1)]
    T[0] = 0

    for price in A:
        for k in range(price, amount + 1):
            T[k] = min(T[k], T[k - price] + 1)

    return T[amount]
