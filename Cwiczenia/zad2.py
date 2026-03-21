"""
1)
a) Scalanie dwoch list jednokierunkowych
b) mergesort na seriach naturalnych

2) wstawianie do kopca binarnego

3) Posortuj tablice k-chaotyczna
T[i] --> T_sorted[j]
j nalezy {i-k, i+k}

4) Posortowana tablica A[n]
i liczba x. Znajdź i,j takie ze
a) A[i] - A[j] = x
b) A[i] + A[j] = x

7) Zliczyc inwersje
i < j , A[i] > A[j]   - to jest to kiedy jest inwersja

8) scalic k posortowanych list o łacznie n elementach
w O(nlogk)

"""


class Node():
    def __init__(self, value):
        self.val = value
        self.next = None


# a)
def scalanie(head1, head2):
    head = Node(0)
    tail = head

    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1 is not None:
        tail.next = head1

    if head2 is not None:
        tail.next = head2

    return head.next


# b)
def roz(A):
    cur = A

    while cur.next is not None and cur.val < cur.next.val:
        cur = cur.next

    j = cur.next
    cur.next = None
    return A, j


def mergesort(A):
    while True:
        result = Node(0)
        i = result
        counter = 0
        while A is not None:
            a, A = roz(A)
            if A is not None:
                b, A = roz(A)
            else:
                b = None
            d = scalanie(a, b)
            i.next = d

            while i.next is not None:
                i = i.next
            counter += 1
        if counter == 1:
            break
        A = result.next
    return result.next


# 2)
def parent(i): return (i - 1) // 2


def wstawianie_do_kopca(T, value):
    T.append(value)
    i = len(T) - 1

    while i > 0 and T[parent(i)] < T[i]:
        # Zamieniamy miejscami z rodzicem
        T[parent(i)], T[i] = T[i], T[parent(i)]
        # Przechodzimy wyżej
        i = parent(i)


# 3)
def heapify_chaotyczne(tablica: list[int], n: int, i: int) -> None:
    max_ind = i
    if left(i) < n and tablica[left(i)] < tablica[max_ind]:
        max_ind = left(i)
    if right(i) < n and tablica[right(i)] < tablica[max_ind]:
        max_ind = right(i)

    if max_ind != i:
        tablica[max_ind], tablica[i] = tablica[i], tablica[max_ind]
        heapify(tablica, n, max_ind)


def build_heap_chaotyczne(tablica: list[int]) -> None:
    n = len(tablica)
    for i in range(parent(n - 1), -1, -1):
        heapify_chaotyczne(tablica, n, i)


def sortowanie_chaotyczne(tablica: list[int]) -> list[int]:
    n = len(tablica)
    build_heap_chaotyczne(tablica)
    for i in range(n - 1):
        tablica[0], tablica[n - 1 - i] = tablica[n - 1 - i], tablica[0]
        heapify(tablica, n - 1 - i, 0)
    return tablica


def tablica_k_chaotyczna(tablica: list[int], k: int) -> None:
    n = len(tablica)
    if n == 0: return

    rozmiar_kopca = min(k+1,n)
    kopiec = tablica[:rozmiar_kopca]
    build_heap_chaotyczne(kopiec)

    indeks = 0

    for i in range(rozmiar_kopca,n):
        tablica[indeks] = kopiec[0]
        indeks += 1

        kopiec[0] = tablica[i]

        heapify_chaotyczne(kopiec,rozmiar_kopca,0)

    while rozmiar_kopca > 0:
        tablica[indeks] = kopiec[0]
        indeks += 1

        kopiec[0] = kopiec[rozmiar_kopca-1]
        rozmiar_kopca -= 1
        heapify_chaotyczne(kopiec,rozmiar_kopca,0)



# 4)
def gasieinca_odejmowanie(T, x):
    N = len(T)
    j = 1
    i = 0
    while j < N:
        if T[j] - T[i] == x:
            return i,j
        elif T[j] - T[i] < x:
            j += 1
        else:
            i += 1
    return None, None


def gasienica_dodawanie(T, x):
    N = len(T)
    i = 0
    j = N - 1

    while i < j :
        if T[i] + T[j] == x:
            return i, j
        elif T[i] + T[j] < x:
            i += 1
        else:
            j -= 1
    return None, None


# 7)
def merge(T, B, p, q, r):
    i = k = p
    j = q
    inwersje = 0

    #  0  1  2  3    4  5
    # [] [] [] | [] [] [] r = 6
    while i < q and j < r:
        if T[i] > T[j]:
            inwersje += q - i
            B[k] = T[j]
            j += 1
        else:
            B[k] = T[i]
            i += 1
        k += 1

    while i < q:
        B[k] = T[i]
        i += 1
        k += 1

    while j < r:
        B[k] = T[j]
        j += 1
        k += 1

    for i in range(p, r):
        T[i] = B[i]

    return inwersje


def mergesort_ultra(T, B, p, r):
    inwersje = 0
    if r - p > 1:
        q = (r + p) // 2
        inwersje += mergesort_ultra(T, B, p, q)
        inwersje += mergesort_ultra(T, B, q, r)
        inwersje += merge(T, B, p, q, r)
    return inwersje


def ile_inwersji(T):
    n = len(T)
    B = [0] * n

    return mergesort_ultra(T, B, 0, n)


# 8)
def parent(i): return (i - 1) // 2


def right(i): return (i * 2) + 2


def left(i): return (i * 2) + 1


def heapify(A, n, i):
    min_ind = i
    if left(i) < n and A[left(i)].val < A[min_ind].val:
        min_ind = left(i)

    if right(i) < n and A[right(i)].val < A[min_ind].val:
        min_ind = right(i)

    if min_ind != i:
        A[min_ind], A[i] = A[i], A[min_ind]
        heapify(A, n, min_ind)


def build_heap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


def zadanie_8(tablica):
    A = []
    for element in tablica:
        if element is not None:
            A.append(element)

    build_heap(A)
    rozmiar = len(A)
    T = []
    while rozmiar > 0:
        T.append(A[0].val)

        if A[0].next is not None:
            A[0] = A[0].next
            heapify(A, rozmiar, 0)
        else:
            A[0] = A[rozmiar - 1]
            rozmiar -= 1
            heapify(A, rozmiar, 0)
