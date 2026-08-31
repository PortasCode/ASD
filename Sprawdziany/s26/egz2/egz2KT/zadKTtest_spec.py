import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 2


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
    (1000, 1000, 500, 5, 6),
    (5000, 5000, 2500, 10, 12),
    (12000, 12000, 6000, 20, 39),
    (30000, 30000, 15000, 50, 85),
    (60000, 60000, 30000, 100, 186),
    (120000, 120000, 60000, 200, 387),
    (250000, 250000, 125000, 500, 995),
    (500000, 500000, 250000, 1000, 1936),
    (1000000, 1000000, 500000, 1000, 2128),
]

def random_float():
    from testy import MY_random, MY_modulus
    return MY_random() / MY_modulus

def random_in_range(a, b):
    from testy import MY_random
    r = random_float()
    while r == 0:
        r = random_float()
    return int(a + (b - a) * r)

def random_shuffle(T):
    from testy import MY_random
    N = len(T)
    for _ in range(N):
        idx1 = MY_random() % N
        idx2 = MY_random() % N
        T[idx1], T[idx2] = T[idx2], T[idx1]

def gentest(n, m, x, k, hint):
    T = [random_in_range(0, m) for _ in range(n)]
    return [T, x, k], hint
