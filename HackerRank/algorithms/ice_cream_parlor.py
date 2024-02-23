from typing import List


def icecream_parlor(m: int, arr: List[int]):
    """Select two flavors of ice cream that will cost all of the money."""
    memo = {}
    for i in range(len(arr)):
        diff = m - arr[i]
        if diff not in memo:
            memo[arr[i]] = i + 1
        else:
            return sorted([i + 1, memo[diff]])
