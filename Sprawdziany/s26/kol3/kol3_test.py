# kol3_test.py
from testy import internal_runtests, limit
from kol3_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return arg #deepcopy(arg)


def printarg(M, T):
    print("Kwota startowa  : ", limit(M))
    print("Transakcje      : ")
    for i in range(min(len(T),10)):
      print( f"   s{i}: {T[i][0]:<4}  e{i}: {T[i][1]:<4}  p{i}: {T[i][2]:<4}  q{i}: {T[i][3]:<4}")
    if len(T) > 10:
        print(" ... ")


def printhint( hint ):
    print("Wynik poprawny  : ", hint)


def printsol( sol ):
    print("Wynik algorytmu : ", sol)


def check(M, T, hint, sol):
    return hint == sol

def generate_tests(num_tests = None):
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


def runtests(f, all_tests = True):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )
