import sys
from random import randint, seed

OIOIOI = False


class Slowo:
    def __init__(self, word: str):
        self.str = word
        self.prev = 0


def merge(NT, B, p, q, r):
    i = k = p
    j = q
    wziete_lewa = 0

    while i < q and j < r:
        if NT[i].str < NT[j].str:
            wziete_lewa += 1
            B[k] = NT[i]
            i += 1
        else:
            NT[j].prev += wziete_lewa
            B[k] = NT[j]
            j += 1
        k += 1

    while i < q:
        B[k] = NT[i]
        i += 1
        k += 1

    while j < r:
        NT[j].prev += wziete_lewa
        B[k] = NT[j]
        j += 1
        k += 1

    for t in range(p, r):
        NT[t] = B[t]


def merge_sort(NT, B, p, r):
    if r - p > 1:
        q = (r + p) // 2
        merge_sort(NT, B, p, q)
        merge_sort(NT, B, q, r)
        merge(NT, B, p, q, r)


def solution(T):
    n = len(T)
    B = [0] * n
    NT = [Slowo(word) for word in T]

    merge_sort(NT, B, 0, n)  # glowne wywolanie funkcji

    return max(object.prev for object in NT)


if __name__ == "__main__":

    def generate_random_string(length):
        return "".join(chr(randint(97, 122)) for _ in range(length))

    if OIOIOI:
        n = int(sys.stdin.readline().strip())
        words = [sys.stdin.readline().strip() for _ in range(n)]
        print(solution(words))
    else:
        seed(1)
        test_def = [
            (10, 5, 10, 6),
            (100, 5, 10, 88),
            (100, 20, 100, 91),
            (10000, 10, 30, 9901),
        ]
        ok = 0
        for idx, (n, m_low, m_high, ans) in enumerate(test_def):
            print("Test", idx + 1)
            words = [generate_random_string(randint(m_low, m_high)) for _ in range(n)]
            result = solution(words)
            if result == ans:
                print("OK")
                ok += 1
            else:
                print("Błąd!")
        print("Wynik:", ok, "/", len(test_def))
