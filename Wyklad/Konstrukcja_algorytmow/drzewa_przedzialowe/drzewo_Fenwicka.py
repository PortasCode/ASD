class BIT:
    def __init__(self, arr):
        self.n = len(arr)
        self.bit = [0] * (self.n + 1)
        for i, v in enumerate(arr):
            self.update(i, v)

    def update(self, i, delta):
        i += 1  # przelicz na 1-based
        while i <= self.n:
            self.bit[i] += delta
            i += i & (-i)  # najniższy ustawiony bit

    def _prefix(self, i):
        i += 1  # przelicz na 1-based
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s

    def query(self, l, r):
        if l == 0:
            return self._prefix(r)
        return self._prefix(r) - self._prefix(l - 1)

    def set_val(self, i, val, old_val):
        """Ustaw arr[i] = val (musisz znać starą wartość)."""
        self.update(i, val - old_val)
