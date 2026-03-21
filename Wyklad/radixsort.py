from math import log2, ceil
def countingsort_radixInt(A:list[int], expo:int):
    n = len(A)
    res = [0] * n
    cnt = [0] * 10

    for i in range(n):
        ind = ( A[i] // expo ) % 10
        cnt[ind] += 1

    for i in range(1, 10):
        cnt[i] += cnt[i - 1]

    for i in range(n-1, -1, -1):
        ind = (A[i] // expo) % 10
        cnt[ind] -= 1
        res[ cnt[ind] ] = A[i]

    for i in range(n):
        A[i] = res[i]

# sortowanie po cyfrach
def radix_sort_int(A:list[int]):
    B = [i for i in A]

    bound = max(B)
    expo = 1
    while bound // expo >= 1:
        countingsort_radixInt(B, expo)
        expo *= 10
    return B


def countingsort_radixChar(A:list[str], ind:int):
    n = len(A)
    res = [''] * n
    cnt = [0] * 128

    for i in range(n):
        p = ord(A[i][ind])
        cnt[p] += 1

    for i in range(1, 128):
        cnt[i] += cnt[i - 1]

    for i in range(n-1, -1, -1):
        p = ord(A[i][ind])
        cnt[p] -= 1
        res[ cnt[p] ] = A[i]

    for i in range(n):
        A[i] = res[i]

# sortowanie po kolenych znakach
def radix_sort_str(A:list[str]):
    B = [a for a in A]
    max_len = max([len(a) for a in B]) - 1
    while max_len > -1:
        countingsort_radixChar(B, max_len)
        max_len -= 1
    return B


def countingsort_radixBIT(A:list[int], bit:int):
    n = len(A)
    res = [0] * n
    cnt = [0] * 65 # mozliwosc w bitach to jest 0 lub 1

    for i in range(n):
        ind = (A[i] >> bit) & 1
        cnt[ind] += 1
    for i in range(1, 65):
        cnt[i] += cnt[i-1]

    for i in range(n-1, -1, -1):
        ind = (A[i] >> bit) & 1
        cnt[ind] -= 1
        res[ cnt[ind] ] = A[i]

    for i in range(n):
        A[i] = res[i]

# sortowanie po bitach liczb
def radix_sort_bit(A:list[int]):
    max_num = max(A)
    B = [a for a in A]

    max_bits = ceil( log2(max_num) )
    bit = 0
    while bit <= max_bits:
        countingsort_radixBIT(B, bit)
        bit += 1
    return B