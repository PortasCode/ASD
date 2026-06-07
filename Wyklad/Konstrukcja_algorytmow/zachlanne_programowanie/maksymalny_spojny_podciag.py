# O(n^3)
def max_subarray_n3(arr):
    n = len(arr)
    max_sum = float("-inf")

    for i in range(n):
        for j in range(i, n):
            current_sum = sum(arr[i : j + 1])
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


# O(n^2)
def max_subarray_n2(arr):
    n = len(arr)
    max_sum = float("-inf")

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


# O(n log n)
def max_subarray_n_log_n(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left_sum = max_subarray_n_log_n(arr, low, mid)
    right_sum = max_subarray_n_log_n(arr, mid + 1, high)

    left_cross_sum = float("-inf")
    temp_sum = 0
    for i in range(mid, low - 1, -1):
        temp_sum += arr[i]
        if temp_sum > left_cross_sum:
            left_cross_sum = temp_sum

    right_cross_sum = float("-inf")
    temp_sum = 0
    for i in range(mid + 1, high + 1):
        temp_sum += arr[i]
        if temp_sum > right_cross_sum:
            right_cross_sum = temp_sum

    cross_sum = left_cross_sum + right_cross_sum

    return max(left_sum, right_sum, cross_sum)


# O(n)
def max_subarray_n(arr):
    max_so_far = float("-inf")
    current_max = 0

    for x in arr:
        current_max += x
        if current_max > max_so_far:
            max_so_far = current_max
        if current_max < 0:
            current_max = 0

    return max_so_far
