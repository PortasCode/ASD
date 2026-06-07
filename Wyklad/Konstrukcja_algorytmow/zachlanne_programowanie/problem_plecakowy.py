def knapsack_2_approx(weights, values, capacity):
    n = len(weights)
    items = []
    for i in range(n):
        ratio = values[i] / weights[i] if weights[i] > 0 else 0
        items.append({"weight": weights[i], "value": values[i], "ratio": ratio})
    items.sort(key=lambda x: x["ratio"], reverse=True)

    greedy_value = 0
    current_weight = 0

    for item in items:
        if current_weight + item["weight"] <= capacity:
            greedy_value += item["value"]
            current_weight += item["weight"]

    max_single_value = 0
    for i in range(n):
        if weights[i] <= capacity and values[i] > max_single_value:
            max_single_value = values[i]

    return max(greedy_value, max_single_value)
