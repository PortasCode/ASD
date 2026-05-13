from functools import cache


def problem_komiwojazera(D: list[list[int]], start: int):
    n = len(D)

    @cache
    def recursion(group: frozenset, city: int):
        if len(group) == 1:
            return D[start][city]

        temp = float("inf")
        poprzednia_grupa = group - frozenset([city])

        for prev_city in poprzednia_grupa:
            koszt = recursion(poprzednia_grupa, prev_city) + D[prev_city][city]
            temp = min(temp, koszt)

        return temp

    wszystkie_miasta = frozenset(range(n)) - frozenset([start])
    result = float("inf")

    for last_city in range(n):
        koszt_calkowity = recursion(wszystkie_miasta, last_city) + D[last_city][start]
        result = min(result, koszt_calkowity)

    return result
