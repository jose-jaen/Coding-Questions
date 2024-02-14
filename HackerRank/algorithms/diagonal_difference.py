from typing import List


def diagonal_difference(arr: List[List[int]]) -> int:
    left_sum = 0
    right_sum = 0
    for i in range(len(arr)):
        left_sum += arr[i][i]
        right_sum += arr[i][len(arr) - 1 - i]
    return abs(left_sum - right_sum)
