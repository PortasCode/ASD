from egz3btesty import runtests


def maze(L: list[str]) -> int:
    n = len(L)

    if L[0][0] == "#" or L[n - 1][n - 1] == "#":
        return -1

    dp = [[-float("inf") for _ in range(n)] for _ in range(n)]

    dp[0][0] = 0

    for i in range(1, n):
        if L[i][0] == ".":
            dp[i][0] = dp[i - 1][0] + 1
        else:
            break

    for col in range(1, n):
        down = [-float("inf")] * n
        up = [-float("inf")] * n

        for row in range(n):
            if L[row][col] == "#":
                continue

            from_left = dp[row][col - 1] + 1

            from_top = down[row - 1] + 1 if row > 0 else -float("inf")

            down[row] = max(from_left, from_top)

        for row in range(n - 1, -1, -1):
            if L[row][col] == "#":
                continue

            from_left = dp[row][col - 1] + 1

            from_bottom = up[row + 1] + 1 if row < n - 1 else -float("inf")

            up[row] = max(from_left, from_bottom)

        for row in range(n):
            dp[row][col] = max(down[row], up[row])

    result = dp[n - 1][n - 1]

    return result if result != -float("inf") else -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
