def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r+1):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j], A[i]
    return i

def qsort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        qsort(A,p,q-1)
        qsort(A,q+1,r)

        """
        tutaj jest szansa pozbyc sie rekurencji ogonowej, czyli takiej ktorej ostatnia operacja to jest wywołanie samej siebie
        while p < r:
            q = partition(A,p,r)
            qodrt(A,p,q-1)
            p = q + 1
        """


