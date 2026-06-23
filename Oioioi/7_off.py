import sys

P = 10**9 + 696969


def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    A = int(data[2])
    B = int(data[3])
    q = int(data[4])
    vals = list(map(int, data[5 : 5 + 3 * q]))

    K = 0
    for i in range(0, len(vals), 3):
        if vals[i] > K:
            K = vals[i]

    CAP = 200000
    SIZE = max(n, m) + (K if K < CAP else CAP) + 6
    if SIZE > CAP:
        SIZE = CAP
    if SIZE < 2:
        SIZE = 2

    inv = [0] * SIZE
    inv[1] = 1
    for i in range(2, SIZE):
        inv[i] = (P - P // i) * inv[P % i] % P

    fact = [1] * SIZE
    for i in range(1, SIZE):
        fact[i] = fact[i - 1] * i % P

    invfact = [1] * SIZE
    invfact[SIZE - 1] = pow(fact[SIZE - 1], P - 2, P)
    for i in range(SIZE - 2, -1, -1):
        invfact[i] = invfact[i + 1] * (i + 1) % P

    def comb(a, b):
        if b < 0 or b > a:
            return 0
        if b == 0 or b == a:
            return 1
        if a < SIZE:
            return fact[a] * invfact[b] % P * invfact[a - b] % P
        if a - b < b:
            b = a - b
        am = a % P
        num = 1
        for i in range(b):
            num = num * ((am - i) % P) % P
        return num * invfact[b] % P

    def f(t, d, L):
        if d == 0:
            return 1
        if t == 0 or L <= 0 or d > t * L:
            return 0
        if L == 1:
            return comb(t, d)
        M = L + 1
        lim = d // M
        tm = t % P

        if t + d < SIZE:
            invf_t1 = invfact[t - 1]
            res = fact[t - 1 + d] * invf_t1 % P * invfact[d] % P
            b1 = 1
            for i in range(1, lim + 1):
                b1 = b1 * ((tm - i + 1) % P) % P * inv[i] % P
                cd = d - i * M
                b2 = fact[t - 1 + cd] * invf_t1 % P * invfact[cd] % P
                term = b1 * b2 % P
                if i & 1:
                    res = (res - term) % P
                else:
                    res = (res + term) % P
            return res % P

        b1arr = [1] * (lim + 1)
        for i in range(1, lim + 1):
            b1arr[i] = b1arr[i - 1] * ((tm - i + 1) % P) % P * inv[i] % P
        cd = d - lim * M
        base = (t + cd - 1) % P
        Num = 1
        for s in range(cd):
            Num = Num * ((base - s) % P) % P
        res = 0
        i = lim
        while i >= 0:
            term = b1arr[i] * (Num * invfact[cd] % P) % P
            if i & 1:
                res = (res - term) % P
            else:
                res = (res + term) % P
            if i:
                add = (t + cd) % P
                for s in range(M):
                    Num = Num * ((add + s) % P) % P
                cd += M
            i -= 1
        return res % P

    HJ = {}
    VJ = {}
    HH = {}
    VH = {}
    Am1 = A - 1
    Bm1 = B - 1
    INF = 1 << 62

    def answer(k, x, y):
        dx = x - 1
        dy = y - 1
        if dx < 0 or dy < 0 or dx > k * A or dy > k * B:
            return 0

        cdx = (dx + A - 1) // A
        cdy = (dy + B - 1) // B

        lo_j = cdy
        hi_j = k - cdx
        if dy < hi_j:
            hi_j = dy
        if k < hi_j:
            hi_j = k
        lo_h = cdx
        hi_h = k - cdy
        if dx < hi_h:
            hi_h = dx
        if k < hi_h:
            hi_h = k

        okj = lo_j <= hi_j
        okh = lo_h <= hi_h
        if not okj and not okh:
            return 0
        cj = (hi_j - lo_j) if okj else INF
        ch = (hi_h - lo_h) if okh else INF

        kmod = k % P
        res = 0

        if cj <= ch:
            lo = lo_j
            hi = hi_j
            hc = HJ.get(dx)
            if hc is None:
                hc = {}
                HJ[dx] = hc
            vc = VJ.get(dy)
            if vc is None:
                vc = {}
                VJ[dy] = vc
            curr = comb(k, lo)
            for j in range(lo, hi + 1):
                t = k - j
                fx = hc.get(t)
                if fx is None:
                    fx = f(t, dx, A)
                    hc[t] = fx
                if fx:
                    fy = vc.get(j)
                    if fy is None:
                        fy = f(j, dy - j, Bm1)
                        vc[j] = fy
                    if fy:
                        res = (res + curr * fx % P * fy) % P
                if j < hi:
                    curr = curr * ((kmod - j) % P) % P * inv[j + 1] % P
        else:
            lo = lo_h
            hi = hi_h
            hc = HH.get(dx)
            if hc is None:
                hc = {}
                HH[dx] = hc
            vc = VH.get(dy)
            if vc is None:
                vc = {}
                VH[dy] = vc
            curr = comb(k, lo)
            for h in range(lo, hi + 1):
                t = k - h
                fy = vc.get(t)
                if fy is None:
                    fy = f(t, dy, B)
                    vc[t] = fy
                if fy:
                    fx = hc.get(h)
                    if fx is None:
                        fx = f(h, dx - h, Am1)
                        hc[h] = fx
                    if fx:
                        res = (res + curr * fx % P * fy) % P
                if h < hi:
                    curr = curr * ((kmod - h) % P) % P * inv[h + 1] % P

        return res % P

    out = []
    qc = {}
    push = out.append
    for i in range(0, len(vals), 3):
        k = vals[i]
        x = vals[i + 1]
        y = vals[i + 2]
        key = (k, x, y)
        a = qc.get(key)
        if a is None:
            a = str(answer(k, x, y))
            qc[key] = a
        push(a)

    sys.stdout.write("\n".join(out))
    sys.stdout.write("\n")


if __name__ == "__main__":
    solve()
