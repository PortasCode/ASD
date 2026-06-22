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


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kunlucky, all_tests=True)
