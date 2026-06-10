def parent(i):
    return (i - 1) // 2


def left(i):
    return i * 2 + 1


def right(i):
    return i * 2 + 2


def heapify_min(T, n, i):
    min_ind = i
    if left(i) < n and T[left(i)] < T[min_ind]:
        min_ind = left(i)
    if right(i) < n and T[right(i)] < T[min_ind]:
        min_ind = right(i)
    if min_ind != i:
        T[min_ind], T[i] = T[i], T[min_ind]
        heapify_min(T, n, min_ind)


def sift_up_min(T, i):
    while i > 0:
        p = parent(i)
        if T[i] < T[p]:
            T[i], T[p] = T[p], T[i]
            i = p
        else:
            break


def moj_push_min(T, value):
    T.append(value)
    sift_up_min(T, len(T) - 1)


def moj_pop_min(T):
    if not T:
        return None
    if len(T) == 1:
        return T.pop()

    wynik = T[0]
    T[0] = T.pop()
    heapify_min(T, len(T), 0)
    return wynik


def heapify_max(T, n, i):
    max_ind = i
    if left(i) < n and T[left(i)] > T[max_ind]:
        max_ind = left(i)
    if right(i) < n and T[right(i)] > T[max_ind]:
        max_ind = right(i)
    if max_ind != i:
        T[max_ind], T[i] = T[i], T[max_ind]
        heapify_max(T, n, max_ind)


def sift_up_max(T, i):
    while i > 0:
        p = parent(i)
        if T[i] > T[p]:
            T[i], T[p] = T[p], T[i]
            i = p
        else:
            break


def moj_push_max(T, value):
    T.append(value)
    sift_up_max(T, len(T) - 1)


def moj_pop_max(T):
    if not T:
        return None
    if len(T) == 1:
        return T.pop()

    wynik = T[0]
    T[0] = T.pop()
    heapify_max(T, len(T), 0)
    return wynik


def ksum(T, k, p):
    if not T or p == 0:
        return 0

    do_usuniecia = [0] * (max(T) + 1)

    kopiec_min = []
    kopiec_max = []
    ile_min = 0  # Zmienna trzymająca PRAWDZIWĄ liczbę elementów bez duchów
    ile_max = 0
    suma = 0

    def czysc_kopiec_min():
        while kopiec_min and do_usuniecia[kopiec_min[0]] > 0:
            do_usuniecia[kopiec_min[0]] -= 1
            moj_pop_min(kopiec_min)

    def czysc_kopiec_max():
        while kopiec_max and do_usuniecia[kopiec_max[0]] > 0:
            do_usuniecia[kopiec_max[0]] -= 1
            moj_pop_max(kopiec_max)

    for i in range(p):
        moj_push_min(kopiec_min, T[i])
        ile_min += 1

    while ile_min > k:
        wartosc = moj_pop_min(kopiec_min)
        moj_push_max(kopiec_max, wartosc)
        ile_min -= 1
        ile_max += 1

    suma += kopiec_min[0]

    for i in range(p, len(T)):
        stary = T[i - p]
        nowy = T[i]

        do_usuniecia[stary] += 1

        if stary >= kopiec_min[0]:
            ile_min -= 1
        else:
            ile_max -= 1

        if nowy >= kopiec_min[0]:
            moj_push_min(kopiec_min, nowy)
            ile_min += 1
        else:
            moj_push_max(kopiec_max, nowy)
            ile_max += 1

        while ile_min > k:
            czysc_kopiec_min()  # Najpierw upewnij się, że nie przerzucasz śmiecia
            wartosc = moj_pop_min(kopiec_min)
            moj_push_max(kopiec_max, wartosc)
            ile_min -= 1
            ile_max += 1

        while ile_min < k:
            czysc_kopiec_max()  # Upewnij się, że z max-kopca wyciągasz legitny element
            wartosc = moj_pop_max(kopiec_max)
            moj_push_min(kopiec_min, wartosc)
            ile_min += 1
            ile_max -= 1

        czysc_kopiec_min()
        suma += kopiec_min[0]

    return suma
