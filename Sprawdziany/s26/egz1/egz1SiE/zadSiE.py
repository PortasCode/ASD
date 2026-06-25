"""
Mateusz Portka 432101


Mialem pomysł, ale niestety chyba nie wyszedł

Plan był taki, żeby dla każdego testu sprawdzać czy mozna go gdzies bezkolizyjne ustalic

    * jeżeli tak to do następnego

    * jeżeli nie to chce wstawić do tej sali gdzie w tym przedziale wartosc studentow mozliwych jest mniejsza
    i sprawdzac czy jezeli najwieksza dotychczasowa wartosc jest wieksza niz to co mozemy osiagnac to zostawiamy a jezeli
    terazniejsza opcja jest lepsza to nadpisujemy

"""

from zadSiEtesty import runtests


def sale_i_egzaminy(E: list[tuple[int, int, int]]):
    n = len(E)
    E.sort(key=lambda x: (x[1], x[0], -x[2]))
    maksymalny_czas = E[-1][1]

    studenci_138 = [0] * (maksymalny_czas + 1)
    studenci_241 = [0] * (maksymalny_czas + 1)

    for i in range(n):
        start, koniec, liczba_studentow = E[i]

        # sala 1.38 jest dostepna w tym terminie
        if sum(studenci_138[start : koniec + 1]) == 0:
            for i in range(start, koniec + 1):
                studenci_138[i] = liczba_studentow

        # sala 2.41 jest dostepna w tym terminie
        elif sum(studenci_241[start : koniec + 1]) == 0:
            for i in range(start, koniec + 1):
                studenci_241[i] = liczba_studentow

        najwieksza_138 = -1
        najwieksza_241 = -1

        for i in range(start, koniec + 1):
            najwieksza_138 = max(najwieksza_138, studenci_138[i])
            najwieksza_241 = max(najwieksza_241, studenci_241[i])

        for i in range(start, koniec + 1):
            studenci_138[i] = najwieksza_138
            studenci_241[i] = najwieksza_241

        if najwieksza_138 > najwieksza_241:
            # bardziej oplaca sie cos podmienic w tablicy 241
            ewentualna_opcja = studenci_241[start - 1] + liczba_studentow
            if ewentualna_opcja > najwieksza_241:
                for i in range(start, koniec + 1):
                    studenci_241[i] = ewentualna_opcja
        else:
            ewentualna_opcja = studenci_138[start - 1] + liczba_studentow
            if ewentualna_opcja > najwieksza_138:
                for i in range(start, koniec + 1):
                    studenci_138[i] = ewentualna_opcja

        print(studenci_138)
        print(studenci_241)
        print()

    return studenci_241[maksymalny_czas] + studenci_138[maksymalny_czas]


runtests(sale_i_egzaminy, all_tests=False)
