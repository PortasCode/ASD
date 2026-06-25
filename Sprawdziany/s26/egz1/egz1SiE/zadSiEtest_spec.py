from testy import MY_random

ALLOWED_TIME = 10


# format testow
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
    [0, 0, 20, 0, 0, 15],
    [1, 50, 20, 7, 30, 254],
    [2, 50, 75, 10, 80, 1164],
    [3, 50, 100, 20, 50, 663],
    [4, 250, 100, 15, 100, 3402],
    [5, 250, 500, 30, 200, 10242],
    [6, 250, 1500, 100, 300, 14735],
    [7, 500, 500, 60, 500, 28301],
    [8, 500, 1000, 90, 800, 45702],
    [9, 500, 1500, 120, 1000, 62812],
]


def generate_instance(n, T, max_len, max_students):
    E = []

    for _ in range(n):
        length = 1 + MY_random() % max_len
        if length > T + 1:
            length = T + 1

        start = MY_random() % (T - length + 2)
        end = start + length - 1
        start += 1
        end += 1
        students = 1 + MY_random() % max_students
        E.append((start, end, students))

    E.sort( key = lambda x: x[1] )
    return E


def gentest(id, n, T, max_len, max_students, hint):
    if id == 0:
        E = [
            (1, 10, 5),
            (11, 20, 4),
            (5, 15, 6),
            (5, 15, 1),
        ]        
        E.sort( key = lambda x: x[1] )
        return (E,), hint

    return (generate_instance(n, T, max_len, max_students),), hint
