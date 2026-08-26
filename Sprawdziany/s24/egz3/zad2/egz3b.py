from egz3btesty import runtests

"""
Złożoność podstawowa O(n^2)


def kunlucky_(T:list[int], k:int):
    n = len(T)

    unlucky_nums = set()
    x = k
    i = 1
    while x <= n:
        unlucky_nums.add(x)
        x = x + (x % i) + 7
        i += 1

    max_len = 0

    for left in range(n):
        unlucky_count = 0
        for right in range(left, n):
            if T[right] in unlucky_nums:
                unlucky_count += 1

            if unlucky_count > 2:
                break

            max_len = max(max_len, right - left + 1)

    return max_len

"""
"""
Złożoność średnia O(nlogn)
"""


def kunlucky(T: list[int], k: int):
    n = len(T)

    unlucky_nums = set()
    x = k
    i = 1
    while x <= n:
        unlucky_nums.add(x)
        x = x + (x % i) + 7
        i += 1

    prefiks = [0 for _ in range(n)]
    if T[0] in unlucky_nums:
        prefiks[0] = 1

    for i in range(1, n):
        prefiks[i] = prefiks[i - 1]
        if T[i] in unlucky_nums:
            prefiks[i] += 1

    result = 0

    for right in range(n):
        bs_left = 0
        bs_right = right

        while bs_left <= bs_right:
            mid = (bs_left + bs_right) // 2

            pechowe_przedzial = (
                prefiks[right] if mid == 0 else prefiks[right] - prefiks[mid - 1]
            )

            if pechowe_przedzial > 2:
                bs_left = mid + 1
            else:
                result = max(result, right - mid + 1)

                bs_right = mid - 1

    return result


"""
Złożoność wzorcowa O(n)


def kunlucky(T: list[int], k: int):
    n = len(T)
    unlucky_nums = set()
    x = k
    i = 1
    while x <= n:
        unlucky_nums.add(x)
        x = x + (x % i) + 7
        i += 1

    result = 0
    left = 0
    count = 0

    for right in range(n):
        if T[right] in unlucky_nums:
            count += 1

        while count > 2:
            if T[left] in unlucky_nums:
                count -= 1
            left += 1

        result = max(result, right - left + 1)

    return result

"""

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kunlucky, all_tests=True)
