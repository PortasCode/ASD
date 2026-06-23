def ladowanie_przyczepy(T: list[int], K: int):
    current_sum = 0
    wziete_liczby = 0
    T.sort(reverse=True)
    for element in T:
        if current_sum + element <= K:
            current_sum += element
            wziete_liczby += 1
            if current_sum == K:
                break

    if current_sum == K:
        return wziete_liczby
    return -1

