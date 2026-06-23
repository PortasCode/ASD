from sys import stdin
from collections import deque


def solve() -> int:
    rin = iter(stdin.read().split())
    P = int(next(rin))
    n = int(next(rin))
    A = int(next(rin))
    B = int(next(rin))
    C = int(next(rin))

    leaves: list[tuple[int, int]] = []
    start_ind = -1

    for i in range(n):
        xj = int(next(rin))
        ej = int(next(rin))

        leaves.append((xj, ej))

        if xj == 0:
            start_ind = i

    if start_ind == -1:
        return -1

    queue = deque([(start_ind, leaves[start_ind][1], 0)])
    max_energy = [-1] * n
    max_energy[start_ind] = leaves[start_ind][1]

    while queue:
        curr_ind, curr_en, steps = queue.popleft()
        curr_x = leaves[curr_ind][0]

        dist_P = abs(curr_x - P)
        cost_P = A * dist_P**2 + B * dist_P + C

        if curr_en >= cost_P:
            return steps + 1

        for next_ind in range(n):
            next_x, next_en = leaves[next_ind]

            if next_ind == curr_ind:
                continue
            if next_x <= curr_x:
                continue

            dist = abs(curr_x - next_x)
            cost = A * dist**2 + B * dist + C

            if curr_en >= cost:
                new_energy = curr_en - cost + next_en

                # relaksacja
                if new_energy > max_energy[next_ind]:
                    max_energy[next_ind] = new_energy
                    queue.append((next_ind, new_energy, steps + 1))

    return -1


if __name__ == "__main__":
    print(solve())
    pass
