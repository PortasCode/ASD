#Złozoność tego algorytmu jest (H)(nlogn)
def merge(A, B, p, q, r):
    i = k = p
    j = q

    while i < q and j < r:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
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


def msort(A):
    n = len(A)
    B = [0] * n
    mergesort(A, B, 0, n)
