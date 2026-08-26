from egz1btesty import runtests

"""
Złożoność najgorsza O(n^3logn)

def kstrong(T: list[int], k: int):
    n = len(T)

    result = 0
    for i in range(1, n + 1):
        for j in range(i):
            tablica = T[j:i]
            tablica.sort()
            suma = 0
            if i - j <= k:
                for element in tablica[::-1]:
                    if element > 0:
                        suma += element
            else:
                suma = sum(tablica[k:])
                for idx in range(k - 1, -1, -1):
                    if tablica[idx] > 0:
                        suma += tablica[idx]

            result = max(result, suma)

    return result

"""

"""
Złożoność średnia O(n^2logn)


def parent(i):
    return (i - 1) // 2


def left(i):
    return i * 2 + 1


def right(i):
    return i * 2 + 2


def sift_up(A, i):
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def sift_down(A, n, i):
    max_idx = i
    l = left(i)
    r = right(i)

    if l < n and A[l] > A[max_idx]:
        max_idx = l
    if r < n and A[r] > A[max_idx]:
        max_idx = r

    if max_idx != i:
        A[i], A[max_idx] = A[max_idx], A[i]
        sift_down(A, n, max_idx)


def push(A, val):
    A.append(val)
    sift_up(A, len(A) - 1)


def pop(A):
    A[0], A[-1] = A[-1], A[0]
    result = A.pop()

    if len(A) > 0:
        sift_down(A, len(A), 0)
    return result


def kstrong(T: list[int], k: int):
    n = len(T)
    if n == 0:
        return 0

    best_result = float("-inf")

    for i in range(n):
        kopiec = []
        suma_przedzialu = 0
        suma_usunietych = 0

        for j in range(i, n):
            val = T[j]
            suma_przedzialu += val

            if val < 0:
                push(kopiec, val)
                suma_usunietych += val

                if len(kopiec) > k:
                    usuniety = pop(kopiec)
                    suma_usunietych -= usuniety

            aktualny_zysk = suma_przedzialu - suma_usunietych

            if aktualny_zysk > best_result:
                best_result = aktualny_zysk

    return best_result


"""
"""
Złozoność wzorcowa O(nk)
"""


def kstrong(T: list[int], k: int):
    T = [0] + T
    n = len(T)

    dp = [[-float("inf") for _ in range(k + 1)] for _ in range(n)]

    dp[1][0] = T[1]
    for i in range(2, n):
        dp[i][0] = max(T[i], dp[i - 1][0] + T[i])

    for i in range(1, n):
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j] + T[i])

    result = -float("inf")
    for i in range(n):
        for j in range(k + 1):
            if dp[i][j] > result:
                result = dp[i][j]
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kstrong, all_tests=True)
