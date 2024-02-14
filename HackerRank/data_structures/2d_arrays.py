from typing import List


def hourglass_sum(arr: List[List[int]]) -> int:
    max_value = -99
    for i in range(4):
        for j in range(4):
            upper = sum(arr[i][j:j + 3])
            lower = sum(arr[i + 2][j:j + 3])
            medium = arr[i + 1][j + 1]
            block_sum = upper + lower + medium

            # Update maximum sum
            if max_value < block_sum:
                max_value = block_sum
    return max_value
