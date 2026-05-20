"""
Mnożenie macierzy, napisac algorytm ktory zwroci nam najmniejszy koszt operacji aby wszystkie wymnozyc
"""


def main_function(A: list[int]):
    n = len(A) - 1  # liczba macierzy

    dp = [[float("inf") for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1  # koniec przedziału

            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j], dp[i][k] + dp[k + 1][j] + (A[i] * A[k + 1] * A[j + 1])
                )

    # Zwracamy wynik dla łańcucha od pierwszej (0) do ostatniej (n-1) macierzy
    return dp[0][n - 1]
