# kol3_spec.py

ALLOWED_TIME = 2


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
    (-1, -1, -1, -1),
    (5, 30, 20, 60),
    (10, 100, 20, 115),
    (100, 100, 20, 321),
    (1000, 1000, 20, 8276),
    (2000, 1000, 20, 11932),
    (6000, 1000, 20, 17470),
    (6000, 1000, 20, 18933),
    (10000, 1000, 100, 29220),
    (100000, 10000, 1000, 916504),
]


def gentest(n, t, M, hint):
    if n == -1:
        M = 8
        T = [
            (1, 4, 5, 7), # T0
            (3, 52, 6, 17), # T1
            (50, 55, 10, 20) # T2
        ]
        hint = 20
        return [M, T], hint

    from testy import MY_random

    T = []
    i = 0 
    while i < n:
        s = MY_random() % t
        e = MY_random() % t
        if s==e: continue
        s,e = min(s,e), max(s,e)
        p = MY_random() % (M+s)
        q = MY_random() % (M+e)
        p,q = min(p,q), max(p,q)
        T.append( (s,e,p,q) )
        i += 1

    return [M,T], hint

