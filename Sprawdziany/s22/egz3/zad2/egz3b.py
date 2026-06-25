from egz3btesty import runtests


def maze(L):
    n = len(L)

    if L[0][0] == "#":
        return -1

    dp = [[-1 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0

    for r in range(1, n):
        if L[r][0] == "#":
            break
        if dp[r - 1][0] != -1:
            dp[r][0] = dp[r - 1][0] + 1

    for c in range(1, n):
        Wejscie = [-1] * n

        for r in range(n):
            if L[r][c] != "#" and dp[r][c - 1] != -1:
                Wejscie[r] = dp[r][c - 1] + 1

        W_dol = [-1] * n
        for r in range(n):
            if L[r][c] == "#":
                continue
            W_dol[r] = Wejscie[r]

            if r > 0 and W_dol[r - 1] != -1:
                W_dol[r] = max(W_dol[r], W_dol[r - 1] + 1)

        W_gore = [-1] * n
        for r in range(n - 1, -1, -1):
            if L[r][c] == "#":
                continue

            W_gore[r] = Wejscie[r]

            if r < n - 1 and W_gore[r + 1] != -1:
                W_gore[r] = max(W_gore[r], W_gore[r + 1] + 1)

        for r in range(n):
            dp[r][c] = max(W_dol[r], W_gore[r])

    return dp[n - 1][n - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
