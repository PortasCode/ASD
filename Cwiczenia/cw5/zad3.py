# to było zadnaie z tym uniwersalnym ujściem na reprezentacji macierzowej grafu

# O(n^2)
def ujscie_kwadrat(G: list[list[int]]):
    n = len(G)

    for i in range(n):
        flaga = True
        if sum(G[i]) != 0:
            continue
        for j in range(n):
            if i == j:
                if G[j][i] != 0:
                    flaga = False
                    break
            else:
                if G[j][i] != 1:
                    flaga = False
                    break

        if flaga:
            return i
    return -1


# O(n)
def ujscie_liniwoe(G: list[list[int]]):
    n = len(G)
    i = 0
    j = 1
    while i < n and j < n:
        if G[i][j] == 1:
            i += 1
        else:
            j += 1

    if i == n:
        return -1

    kandydat = i
    for j in range(n):
        if G[kandydat][j] == 1:
            return -1

        if j != kandydat and G[j][kandydat] == 0:
            return -1
    return kandydat
