from random import randint


def qsort(A: list[int], p: int, r: int):
    if p < r:
        #q = lomuto_partition(A, p, r)
        q = hoares_partition(A, p, r)
        qsort(A, p, q)  # qsort(A, p, q-1)
        qsort(A, q + 1, r)


# Lomuto partition function
def lomuto_partition(A: list[int], p: int, r: int):
    x_ind = randint(p, r)
    x = A[x_ind]
    A[r], A[x_ind] = A[x_ind], A[r]
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    return i


# Hoares partition function - nadal liniowa ale szybsza bo mniej porownan
def hoares_partition(A: list[int], p: int, r: int):
    x = A[randint(p, r)]
    i = p - 1;
    j = r + 1

    while True:
        while True:
            i += 1
            if A[i] >= x: break

        while True:
            j -= 1
            if A[j] <= x: break

        if i >= j:
            return j

        A[i], A[j] = A[j], A[i]


def quick_sort(A: list[int]):
    n: int = len(A)
    B = [i for i in A]
    qsort(B, 0, n - 1)
    return B
