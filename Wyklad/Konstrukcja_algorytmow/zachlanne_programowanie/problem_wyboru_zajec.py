def problem_wyboru_zajec(A: list[tuple[int, int]]) -> int:

    A.sort(key=lambda x: x[1])

    result = 0
    last_meta = -1

    for start, meta in A:
        if start >= last_meta:
            last_meta = meta
            result += 1

    return result
