"""
Max i min - Dany jest ciąg liczb naturalnych, dzielimy go na k czesci tak aby najmnejsza suma z tych k-tych podzialow byla najwieksza
"""


def main_function(A: list[int], k: int):
    n = len(A)
    if n < k:
        return -1

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + A[i]

    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = prefix[i]

    for j in range(2, k + 1):
        for i in range(j, n + 1):
            best_split_score = 0
            for m in range(j - 1, i):
                last_interval_sum = prefix[i] - prefix[m]

                current_split_score = min(dp[m][j - 1], last_interval_sum)

                if current_split_score > best_split_score:
                    best_split_score = current_split_score

            dp[i][j] = best_split_score

    return dp[n][k]
