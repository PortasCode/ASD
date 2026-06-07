from collections import defaultdict, Counter
import heapq


class Node:
    def __init__(self, value, znak=None):
        self.right = None
        self.left = None
        self.symbol = znak
        self.val = value

    def __lt__(self, other):
        return self.val < other.val


def kody_Hoffmana(tekst: str):
    slownik_liter = defaultdict(lambda: 0)
    # slownik_liter = Counter(tekst) to jest alternatywne rozwiazanie

    tekst = tekst.lower()

    for znak in tekst:
        slownik_liter[znak] += 1

    kopiec = []
    for key, value in slownik_liter.items():
        heapq.heappush(kopiec, Node(value, key))

    while len(kopiec) > 1:
        lewy = heapq.heappop(kopiec)
        prawy = heapq.heappop(kopiec)

        suma_wartosci = lewy.val + prawy.val
        rodzic = Node(suma_wartosci, None)
        rodzic.left = lewy
        rodzic.right = prawy

        heapq.heappush(kopiec, rodzic)

    korzen = kopiec[0]

    slownik_kodow = defaultdict(lambda: "")

    def rekurencyjne_kody(curr: Node, path: str):
        if curr.symbol is not None:
            slownik_kodow[curr.symbol] = path
            return

        if curr.left != None:
            rekurencyjne_kody(curr.left, path + "0")

        if curr.right != None:
            rekurencyjne_kody(curr.right, path + "1")
