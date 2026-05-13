def lis(A: list[int]):
    n = len(A)
    F = [1] * n
    P = [-1] * n

    for k in range(1, n):
        for i in range(k):
            if A[i] < A[k] and F[k] < F[i] + 1:
                F[k] = F[i] + 1
                P[k] = i
    return max(F)
