from egz2btesty import runtests


def magic(C):
    n = len(C)
    if n == 0:
        return -1

    dp = [-1] * n
    dp[0] = 0

    for i in range(n - 1):
        if dp[i] == -1:
            continue

        current_gold = dp[i]
        G = C[i][0]
        doors = C[i][1:]

        for K, W in doors:
            if W == -1 or W <= i:
                continue

            if G <= K:
                gold_needed = K - G

                if current_gold >= gold_needed:
                    gold_carried_to_next = current_gold - gold_needed

                    if gold_carried_to_next > dp[W]:
                        dp[W] = gold_carried_to_next

            else:
                gold_to_remove = G - K

                if gold_to_remove <= 10:
                    gold_carried_to_next = current_gold + gold_to_remove

                    if gold_carried_to_next > dp[W]:
                        dp[W] = gold_carried_to_next

    return dp[n - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=True)
