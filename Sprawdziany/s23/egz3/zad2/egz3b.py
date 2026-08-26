from egz3btesty import runtests


def uncool(P: list[tuple[int, int]]):
    n = len(P)
    tablica = [(P[i], i) for i in range(n)]

    tablica.sort(key=lambda x: (x[0][0], -x[0][1]))

    max_interval_data, max_index = tablica[0]
    max_end = max_interval_data[1]

    for i in range(1, n):
        curr_interval_data, curr_index = tablica[i]
        curr_start, curr_end = curr_interval_data

        if curr_start <= max_end and curr_end > max_end:
            return max_index, curr_index

        if curr_start > max_end:
            max_end = curr_end
            max_index = curr_index

    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(uncool, all_tests=True)
