from typing import List


def compare_triplets(a: List[int], b: List[int]) -> List[int]:
    res = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            res[0] += 1
        elif a[i] < b[i]:
            res[1] += 1
    return res
