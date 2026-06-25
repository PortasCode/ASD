from egz3atesty import runtests


def snow(T: int, I: list[tuple[int, int]]):
    events = []

    for a, b in I:
        events.append((a, 1))
        events.append((b + 1, -1))

    events.sort()

    max_snow = 0
    current_snow = 0

    for pos, value in events:
        current_snow += value
        if current_snow > max_snow:
            max_snow = current_snow

    return max_snow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
