from kol1_test import runtests

"""
Złożoność średnia O(nlog^2(n))

def k_big(A: list[int], k: int) -> int:
    A.sort()
    n = len(A)

    left = 1
    right = A[-1] * A[-1]

    ans = 1

    while left <= right:
        mid = (left + right) // 2
        licznik = 0

        for i in range(n):
            lewa = 0
            prawa = n - 1
            pierwszy_wiekszy = n

            while lewa <= prawa:
                srodek = (lewa + prawa) // 2

                if A[i] * A[srodek] >= mid:
                    pierwszy_wiekszy = srodek
                    prawa = srodek - 1
                else:
                    lewa = srodek + 1

            licznik += n - pierwszy_wiekszy

        if licznik >= k:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans
"""

"""
Złożoność wzorcowa O(nlogn)
"""


def k_big(A: list[int], k: int) -> int:
    A.sort()
    n = len(A)

    left = 1
    right = A[-1] * A[-1]
    ans = 1

    while left <= right:
        mid = (left + right) // 2
        licznik = 0
        lewa = 0
        prawa = n - 1

        while lewa < n and prawa >= 0:
            if A[lewa] * A[prawa] < mid:
                lewa += 1
            else:
                licznik += n - lewa
                prawa -= 1

        if licznik >= k:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(k_big, all_tests=True)
