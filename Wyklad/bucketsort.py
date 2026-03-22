def insert_sort(A:list[float]):
    for i in range(1, len(A)):
        key = A[i]
        j = i- 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j+1] = key


# to jest sortowanie dla liczb z przedziału [0,1)
def bucket_sort(A:list[float]):
    n = len(A)
    B = [x for x in A]

    buckets = [[] for _ in range(n)]
    for x in B:
        b_ind = int(x * n)
        buckets[b_ind].append(x)

    for bucket in buckets:
        insert_sort(bucket)
    ind = 0
    for bucket in buckets:
        for x in bucket:
            B[ind] = x
            ind += 1
    return B