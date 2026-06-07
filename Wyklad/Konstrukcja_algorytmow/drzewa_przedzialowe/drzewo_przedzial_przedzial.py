class LazySegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(arr, 1, 0, self.n - 1)

    def _build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = arr[l]
            return
        mid = (l + r) // 2
        self._build(arr, 2 * node, l, mid)
        self._build(arr, 2 * node + 1, mid + 1, r)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _push_down(self, node, l, r):
        if self.lazy[node] == 0:
            return
        mid = (l + r) // 2
        d = self.lazy[node]
        self.tree[2 * node] += d * (mid - l + 1)
        self.tree[2 * node + 1] += d * (r - mid)
        self.lazy[2 * node] += d
        self.lazy[2 * node + 1] += d
        self.lazy[node] = 0

    def range_update(self, ql, qr, delta, node=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.tree[node] += delta * (r - l + 1)
            self.lazy[node] += delta
            return
        self._push_down(node, l, r)
        mid = (l + r) // 2
        self.range_update(ql, qr, delta, 2 * node, l, mid)
        self.range_update(ql, qr, delta, 2 * node + 1, mid + 1, r)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, ql, qr, node=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        self._push_down(node, l, r)
        mid = (l + r) // 2
        return self.query(ql, qr, 2 * node, l, mid) + self.query(
            ql, qr, 2 * node + 1, mid + 1, r
        )
