from egz2atesty import runtests


def wired(T):
    n2 = len(T)
    memo = {}

    def dp(i, j):
        if i > j:
            return 0

        if (j - i + 1) % 2 != 0:
            return float("inf")

        if (i, j) in memo:
            return memo[(i, j)]

        min_cost = float("inf")

        for k in range(i + 1, j + 1, 2):
            current_cable_cost = 1 + abs(T[i] - T[k])

            total_cost = current_cable_cost + dp(i + 1, k - 1) + dp(k + 1, j)

            if total_cost < min_cost:
                min_cost = total_cost

        memo[(i, j)] = min_cost
        return min_cost

    return dp(0, n2 - 1)


T = [7, 1, 3, 7, 2, 1]
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wired, all_tests=True)
