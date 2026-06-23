from egz1atesty import runtests


def snow(S: list[int]):
    S.sort(reverse=True)
    n = len(S)

    indeks = 0
    topnienie = 0
    result = 0

    while indeks < n:
        if S[indeks] - topnienie > 0:
            result += S[indeks] - topnienie
            topnienie += 1
            indeks += 1
        else:
            break

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
