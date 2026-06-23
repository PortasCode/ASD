from egz1btesty import runtests


class Node:
    def __init__(self):
        self.left = None  # lewe poddrzewo
        self.right = None  # prawe poddrzewo
        self.x = None  # pole do wykorzystania przez studentow


def widentall(T):
    if not T:
        return 0

    poziomy = {}

    def zlicz_poziomy(wezel, glebokosc):
        if not wezel:
            return
        if glebokosc not in poziomy:
            poziomy[glebokosc] = 0
        poziomy[glebokosc] += 1

        zlicz_poziomy(wezel.left, glebokosc + 1)
        zlicz_poziomy(wezel.right, glebokosc + 1)

    zlicz_poziomy(T, 0)

    docelowy_poziom = 0
    max_szerokosc = 0

    for poziom, szerokosc in poziomy.items():
        if szerokosc > max_szerokosc or (
            szerokosc == max_szerokosc and poziom > docelowy_poziom
        ):
            max_szerokosc = szerokosc
            docelowy_poziom = poziom

    def tnij(wezel, aktualny_poziom):
        if not wezel:
            return 0, False

        if aktualny_poziom == docelowy_poziom:
            ciecia = 0
            if wezel.left:
                ciecia += 1
            if wezel.right:
                ciecia += 1
            return ciecia, True

        ciecia_lewe, dociera_lewe = tnij(wezel.left, aktualny_poziom + 1)
        ciecia_prawe, dociera_prawe = tnij(wezel.right, aktualny_poziom + 1)

        calkowite_ciecia = 0
        czy_my_docieramy = False

        if wezel.left:
            if dociera_lewe:
                calkowite_ciecia += ciecia_lewe
                czy_my_docieramy = True
            else:
                calkowite_ciecia += 1

        if wezel.right:
            if dociera_prawe:
                calkowite_ciecia += ciecia_prawe
                czy_my_docieramy = True
            else:
                calkowite_ciecia += 1

        return calkowite_ciecia, czy_my_docieramy

    wynik_ciec, _ = tnij(T, 0)

    return wynik_ciec


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(widentall, all_tests=True)
