from testy import *
from zadSiEtest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg(arg):
    return deepcopy(arg)


def printarg(E):
    print("Liczba egzaminow : ", len(E))
    print("E                : ", limit(E))


def printhint(hint):
    print("Wynik poprawny   : ", hint)


def printsol(sol):
    print("Wynik algorytmu  : ", sol, end="\n")


def check(E, hint, sol):
    return hint == sol


def generate_tests(num_tests=None):
    global TEST_SPEC
    TESTS = []

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    return TESTS


def runtests(f, all_tests=True):
    internal_runtests(copyarg, printarg, printhint, printsol, check,
                      generate_tests, all_tests, f, ALLOWED_TIME)
