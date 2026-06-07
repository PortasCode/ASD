"""
Problem komiwojazera:
    - zakladamy ze istnieje bezposrednie polaczenie miedzy kazda para wierzcholkow

[ O(2^n * n^2) ]
"""

graph_matrix = list[list[int]]


def tsp(graph: graph_matrix):
    n = len(graph)

    if 0 <= n <= 1:
        return 0

    # maski bitowe jako sposob na zapisanie ktory wierzcholek nalezy do zbioru
    dp = [[float("inf") for _ in range(n)] for _ in range(1 << n)]

    dp[1][0] = 0

    for subset in range(1, 1 << n):
        if not (subset & 1):
            continue

        for t in range(1, n):
            if not (subset & (1 << t)):
                continue
            for r in range(n):
                if r == t:
                    continue

                if subset & (1 << r):
                    dp[subset][t] = min(
                        dp[subset ^ (1 << t)][r] + graph[r][t], dp[subset][t]
                    )

    full_subset = (1 << n) - 1
    min_cost = float("inf")

    for t in range(1, n):
        min_cost = min(min_cost, dp[full_subset][t] + graph[t][0])
