# Złozonoscego algorytmu jest O(nlogn)
def parent(i): return (i - 1) // 2


def left(i):    return i * 2 + 1


def right(i): return i * 2 + 2


def heapify(A, n, i):
    max_ind = i
    if left(i) < n and A[left(i)] > A[max_ind]:
        max_ind = left(i)

    if right(i) < n and A[right(i)] > A[max_ind]:
        max_ind = right(i)

    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind)


def build_heap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):  # przegladanie od ostatniego elementu ktory powinien miec dziecko
        heapify(A, n, i)


def heap_sort(A):
    build_heap(A)
    n = len(A)
    for i in range(0, n - 1):
        A[0], A[n - i - 1] = A[n - i - 1], A[0]
        heapify(A, n - 1, 0)
