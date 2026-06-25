from testy import MY_random, MY_modulus
ALLOWED_TIME = 3


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
    [0,-1,-1],
    [1,20, (1208,1646)],
    [2,50, (2334, 1925)],
    [3,150, (4013, 4668)],
    [4,350, (10962, 13201)],
    [5,500, (15005, 21154)],
    [6,700, (23632, 24869)],
    [7,800, (27429, 30434)],
    [8,900, (30138, 30072)],
    [9,1000, (30994, 38310)],
]


def generate_test(n):

    M = list(range(n))

    for i in range(n - 1, 0, -1):
        j = MY_random() % (i + 1)
        M[i], M[j] = M[j], M[i]

    owner = [0] * n

    for pos, v in enumerate(M):
        owner[v] = pos & 1

    G = [[] for _ in range(n)]
    W = []

    for player in [0, 1]:

        V = [v for v in range(n) if owner[v] == player]

        for i in range(len(V) - 1, 0, -1):
            j = MY_random() % (i + 1)
            V[i], V[j] = V[j], V[i]

        ptr = 0

        while ptr + 5 < len(V):

            length = 6 + MY_random() % 5

            if ptr + length > len(V):
                break

            path = V[ptr:ptr + length]

            ptr += length

            for i in range(length - 1):
                a = path[i]
                b = path[i + 1]

                G[a].append(b)
                G[b].append(a)

            score = 100 + MY_random() % 900

            W.append((path[0], path[-1], score))

    for u in range(n):
        for v in range(u + 1, n):

            found = False

            for x in G[u]:
                if x == v:
                    found = True
                    break

            if found:
                continue

            if MY_random() % 100 < 70:
                G[u].append(v)
                G[v].append(u)

    return G, M, W



def gentest(id,n, hint):    
    from testy import MY_random

    if id==0:
        G = [ [7, 6],      # 0
              [4],         # 1
              [4],         # 2
              [4,6],       # 3
              [7,1,2,5,3], # 4
              [4],         # 5
              [7,0,3],     # 6
              [4,8,0,6],   # 7
              [7] ]        # 8
        
        M = [5, 0, 2, 6, 1, 7, 3, 8, 4 ]
        W = [(2,3,4), (1,5,2), (8,7,3), (0,6,8)]
        return ((G,M,W), (12,19))

    else:
        return generate_test(n), hint


    data=None
    return data, hint
