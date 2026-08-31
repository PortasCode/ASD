from testy import *
from zadKTtest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return arg #deepcopy(arg)


def printarg( T, x, k ):
    print("Tablica : ", limit(T))
    print("x       : ", limit(x))
    print("k       : ", limit(k))


def printhint( hint ):
    print("Wynik poprawny       : ", hint)


def printsol( sol ):
    print("Wynik algorytmu     : ", sol)


def check( T, x, k, hint, sol ):
    return hint == sol

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    T = [7, 1, 9, 6, 1, 8, 2, 10]
    x = 4
    k = 3
    hint = 5
    newtest = {}
    newtest["arg"] = [T, x, k]
    newtest["hint"] = hint
    TESTS.append(newtest)

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    return TESTS


def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

