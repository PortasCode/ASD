from testy import MY_random, MY_modulus
ALLOWED_TIME = 3


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# (|cities|, |flights|, |resorts|, sol)
    [0, -1,-1,-1, -1],
    [1, 10,20, 0.1,11],
    [2, 50,20, 0.3,74],
    [3, 50,50, 0.3,291],
    [4, 40,100, 0.3,50 ],
    [5, 80,60, 0.5,24],
    [6, 70,70, 0.2,1299],
    [7, 10,300, 0.2,428],
    [8, 300,10, 0.2,398],
    [9, 2,4000, 0.01,1041],
#    [1, 200,100, 0.3,-1],
#    [1, 500,100, 0.3,-1],
#    [1, 500,1000, 0.3,-1],
]




def generate_instance(n, m, alpha):
    edges = []

    # ------------------------------------------------------------
    # 1. Losowe drzewo na n superwierzchołkach
    # ------------------------------------------------------------
    tree_edges = []
    for v in range(1, n):
        parent = MY_random() % v
        tree_edges.append((parent, v))

    # ------------------------------------------------------------
    # 2. Zastępowanie każdego superwierzchołka spójnym grafem
    # ------------------------------------------------------------
    blocks = []     # lista wierzchołków należących do każdego bloku
    next_id = 0

    for _ in range(n):

        size = m // 2 + (MY_random() % (m - m // 2 + 1))

        verts = list(range(next_id, next_id + size))
        next_id += size

        blocks.append(verts)

        local_edges = set()

        # --- najpierw losowe drzewo (spójność)
        for i in range(1, size):
            p = MY_random() % i
            a = verts[i]
            b = verts[p]

            if a > b:
                a, b = b, a

            local_edges.add((a, b))

        # --- docelowa liczba krawędzi
        max_edges = size * (size - 1) // 2
        target_edges = int(alpha * max_edges)

        if target_edges < size - 1:
            target_edges = size - 1

        # --------------------------------------------------------
        # Dodawanie dodatkowych krawędzi.
        # Preferujemy krótkie połączenia w obrębie bloku,
        # co daje bardziej "lokalną" strukturę.
        # --------------------------------------------------------
        while len(local_edges) < target_edges:

            i = MY_random() % size

            # losujemy odległość 1..size-1
            dist = 1 + (MY_random() % (size - 1))

            if MY_random() % 2:
                j = i + dist
            else:
                j = i - dist

            if j < 0 or j >= size:
                continue

            a = verts[i]
            b = verts[j]

            if a > b:
                a, b = b, a

            local_edges.add((a, b))

        edges.extend(local_edges)

    # ------------------------------------------------------------
    # 3. Krawędzie między blokami zgodne z drzewem bazowym
    # ------------------------------------------------------------
    for a, b in tree_edges:

        va = blocks[a][MY_random() % len(blocks[a])]
        vb = blocks[b][MY_random() % len(blocks[b])]

        if va > vb:
            va, vb = vb, va

        edges.append((va, vb))

    return edges





def gentest(id,n, m, alpha, hint):    
    from testy import MY_random

    if id==0:
        G = [ (0,1), (1,2), (7,1), 
              (7,2), (6,7), (2,3),
              (4,3), (4,8), (4,5), 
              (3,8), (5,8) ]
        return (G,), 1

    else:
        return (generate_instance(n,m, alpha),), hint


    data=None
    return data, hint
