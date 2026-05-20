def najdluzszy_rosnacy_podciag(F: list[int]):
    n = len(F)
    T = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if F[i] > F[j]:
                T[i] = max(T[i], T[j] + 1)

    return max(T)


def najdluzszy_rosnacy_podciag_v2(F: list[int]):
    if not F:
        return 0

    n = len(F)
    T = [F[0]]

    for i in range(1, n):
        number = F[i]
        left = 0
        right = len(T) - 1

        while left <= right:
            mid = (left + right) // 2

            if number > T[mid]:
                left = mid + 1
            else:
                right = mid - 1

        if left < len(T):
            T[left] = number
        else:
            T.append(number)

    return len(T)
