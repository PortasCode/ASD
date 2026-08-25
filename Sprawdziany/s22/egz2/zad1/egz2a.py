from egz2atesty import runtests
import math


class DrzewoPrzedzialMax:
    def __init__(self, n: int, N: int, T: int):
        self.drzewo = [0] * (2 * N)
        self.N = N

        for idx in range(1, 2 * N):
            self.drzewo[idx] = T

    def _update(self, value: int) -> int:
        idx = 1

        while idx < self.N:
            if self.drzewo[2 * idx] >= value:
                idx = 2 * idx
            else:
                idx = 2 * idx + 1

        result = idx
        self.drzewo[result] -= value

        idx = (idx) // 2

        while idx > 0:
            self.drzewo[idx] = max(self.drzewo[2 * idx], self.drzewo[2 * idx + 1])
            idx //= 2

        return result - self.N


def coal(A: list[int], T: int):
    n = len(A)
    N = 1

    while N < n:
        N *= 2

    drzewo = DrzewoPrzedzialMax(n, N, T)

    result = -1
    for idx in range(n):
        transport = A[idx]

        temp = drzewo._update(transport)

        if idx == n - 1:
            result = temp

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(coal, all_tests=True)
