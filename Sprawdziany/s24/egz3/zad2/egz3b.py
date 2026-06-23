from egz3btesty import runtests


def kunlucky(T, k):
    n = len(T)
    najwieksza_liczba = max(T)

    current = k
    pechowe_liczby = [current]
    licznik = 1
    while current <= najwieksza_liczba:
        current = current + (current % licznik) + 7
        pechowe_liczby.append(current)
        licznik += 1

    pechowe_liczby = set(pechowe_liczby)

    poczatek = 0
    koniec = 1
    result = 0
    counter = 0 if T[0] not in pechowe_liczby else 1

    while koniec < n:
        if counter <= 2:
            dlugosc = koniec - poczatek
            result = max(result, dlugosc)

            if T[koniec] in pechowe_liczby:
                counter += 1
            koniec += 1
        else:
            if T[poczatek] in pechowe_liczby:
                counter -= 1
            poczatek += 1

    if counter <= 2:
        result = max(result, koniec - poczatek)

    return result


def kunlucky_nlogn(T, k):
    n = len(T)
    najwieksza_liczba = max(T)

    current = k
    pechowe_liczby = [current]
    licznik = 1

    while current <= najwieksza_liczba:
        current = current + (current % licznik) + 7
        pechowe_liczby.append(current)
        licznik += 1

    pechowe_liczby = set(pechowe_liczby)

    Sumy_prefiksowe = [0 for _ in range(n + 1)]

    for i in range(n):
        Sumy_prefiksowe[i + 1] = Sumy_prefiksowe[i]

        if T[i] in pechowe_liczby:
            Sumy_prefiksowe[i + 1] += 1

    result = 0

    for poczatek in range(n):
        left = poczatek
        right = n - 1
        best_koniec = left

        while left <= right:
            mid = (left + right) // 2
            licznik_pecha = Sumy_prefiksowe[mid + 1] - Sumy_prefiksowe[poczatek]

            if licznik_pecha <= 2:
                best_koniec = mid
                left = mid + 1
            else:
                right = mid - 1

        dlugosc = best_koniec - poczatek + 1
        if dlugosc > result:
            result = dlugosc

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kunlucky_nlogn, all_tests=True)
