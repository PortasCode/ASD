class Node:
    def __init__(self, value):
        self.val = value
        self.children = []
        self.F = -1
        self.G = -1

    def f(self):
        if self.F != -1:
            return self.F

        value = self.val
        for u in self.children:
            value += u.g()
        self.F = max(self.g(), value)
        return self.F

    def g(self):
        if self.G != -1:
            return self.G

        self.G = 0
        for u in self.children:
            self.G += u.f()

        return self.G


def main_function(A: list[int], edges: list[tuple[int, int]]):
    n = len(A)
    T = [Node(A[i]) for i in range(n)]

    for parent, child in edges:
        T[parent].children.append(T[child])

    root = T[0]

    return root.f()
