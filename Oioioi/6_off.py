import sys


def main():
    dane_total = sys.stdin.read().strip().split()

    if len(dane_total) == 0:
        return

    dane = list(map(int, dane_total[1:]))
    res = [1, 2, 7]

    while True:
        res.append((3 * res[-1] + res[-2] - res[-3]) % 67)

        if res[-3] == 1 and res[-2] == 2 and res[-1] == 7:
            res.pop()
            res.pop()
            res.pop()
            break

    length = len(res)

    for n in dane:
        print(res[(n - 1) % length])


if __name__ == "__main__":
    main()

