# Ładowanie promu  A - długość aut w korku     Prom ma dwa pasy i ma dlugosc L, auta wybieraja sobie pasy do wjechania, chcemy zmiescic jak najwiecej aut


def ladowanie_promu(A: list[int], L: int):
    n = len(A)

    sums = [0] * n
    sums[0] = A[0]

    for i in range(1, n):
        sums[i] = sums[i - 1] + A[i]

    dp = [[False for _ in range(L + 1)] for _ in range(n + 1)]

    dp[0][0] = True

    max_cars = 0
    for i in range(1, n + 1):
        changed = False
        for l in range(0, L + 1):
            if dp[i - 1][l]:
                if l + A[i - 1] <= L:
                    dp[i][l + A[i - 1]] = True
                    changed = True
                if sums[i - 1] - l <= L:
                    dp[i][l] = True
                    changed = True

        if changed:
            max_cars = i
        else:
            break

    return max_cars
