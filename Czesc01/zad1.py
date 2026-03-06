"""
Zad 1
a) wstawienie do posortowanej listy
b) usuwanie max elementu z listy
c) insert / select sort

Zad 2
min i max z tablicy T[n]
ale uzywajac 3/2 n porownan

Zad 3
Przesuniecie cykliczne tablicy
T[n] w miejscu
T[i] -> T[(i+k)%n]

Zad 4
Rosnacy ciag arytmetyczny
pytamy jakiej liczby brakuje, chcemy jac znalexc jak najszybciej

Zad 5
odwrocic liste odsylaczowa

Zad 6
Chomiki
[a1,b1],[a2,b2],[a3,b3]....[an,bn]
a1 < b1 < a2 < b2 < ... < an < bn
pytamy o minimalna najwieksza odleglosc jak mozemy rozlozyc chomiki

"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


# Zad 1
# a)
def insert(first, node):
    if first is None:
        return node

    prev = None
    cur = first

    while cur is not None:
        if cur.val >= node.val:
            if prev is None:
                node.next = cur
                return node
            else:
                prev.next = node
                node.next = cur
        prev = cur
        cur = cur.next

    prev.next = node
    return first


# napisac to samo na jednej zmiennej


# b)
def remove_max(head) -> tuple[Node, Node]:
    if head is None:
        return (None, None)

    value = head.val
    cur, prev = head, None

    while cur.next is not None:
        if cur.next.val > value:
            value = cur.next.val
            prev = cur
        cur = cur.next

    node = Node(value)
    if prev == None:  # head jest najwieksze
        return (head.next, node)
    prev.next = prev.next.next
    return (head, node)


# c)

# selection sort
def selection_sort(head):
    new_head = None

    while head is not None:
        head, value = remove_max(head)

        if new_head is None:
            new_head = value
        else:
            value.next = new_head
            new_head = value

    return new_head


# Zad 2
def max_and_min(T):
    N = len(T)
    mini = T[0]
    maxi = T[0]

    for i in range(0, N, 2):

        if T[i] < T[i + 1]:
            if T[i] < mini:
                mini = T[i]
            if T[i + 1] > maxi:
                maxi = T[i + 1]
        else:
            if T[i] > maxi:
                maxi = T[i]
            if T[i + 1] < mini:
                mini = T[i + 1]

    return mini, maxi


# Zad 3
def rev(T, s, f):
    while s < f:
        T[s], T[f] = T[f], T[s]
        s += 1
        f -= 1


def move_cyclic(T, k):
    n = len(T)
    l = k % n

    rev(T, 0, n - 1)
    rev(T, 0, l - 1)
    rev(T, l, n - 1)


# Zad 4
def first_missing(T):
    n = len(T)
    left = 0
    right = n - 1
    while left <= right:
        mid = (right + left) // 2
        if T[mid] == mid:
            left = mid + 1
        else:
            right = mid - 1
    return left


# Zad 5
def reverse_linked_list(first):
    cur = first
    if cur.next is None:
        return first

    while cur.next is not None:
        temp = cur.next
        cur.next = temp.next
        temp.next = cur

        cur = cur.next
    cur.next = temp
    return cur

# Zad 6
