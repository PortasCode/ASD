from egz3Atesty import runtests

"""
def treecut(H: list[int], k: int):
    n = len(H)

    counter = 0
    for indeks in range(n):
        for i in range(indeks):
            if H[i] > H[indeks]:
                counter += 1

        if counter > k:
            return indeks

    return n
"""

inwersje = 0


def merge(A, B, p, q, r):
    global inwersje
    i = p
    k = p
    j = q

    while i < q and j < r:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
            inwersje += q - i
        k += 1

    while i < q:
        B[k] = A[i]
        i += 1
        k += 1

    while j < r:
        B[k] = A[j]
        j += 1
        k += 1

    for t in range(p, r):
        A[t] = B[t]


def mergesort(A, B, p, r):
    if r - p > 1:
        q = (r + p) // 2
        mergesort(A, B, p, q)
        mergesort(A, B, q, r)
        merge(A, B, p, q, r)


def treecut(H: list[int], k: int):
    global inwersje
    n = len(H)
    left = 1
    right = n
    best_answer = 0

    while left <= right:
        mid = (left + right) // 2

        NT = H[:mid]
        T = [0] * mid
        inwersje = 0
        mergesort(NT, T, 0, mid)
        if inwersje > k:
            right = mid - 1
        else:
            best_answer = mid
            left = mid + 1

    return best_answer


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(treecut, all_tests=True)
