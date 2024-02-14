from typing import List


def plus_minus(arr: List[int]) -> None:
    """Get ratio of comments."""
    n = len(arr)
    n_positives, n_negatives = [0] * 2
    for i in range(n):
        if arr[i] > 0:
            n_positives += 1
        elif arr[i] < 0:
            n_negatives += 1
    n_zeros = n - n_positives - n_negatives

    # Get proportions
    print(n_positives / n)
    print(n_negatives / n)
    print(n_zeros / n)
