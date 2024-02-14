from typing import List


def mini_max_sum(arr: List[int]) -> None:
    minimum = float('inf')
    maximum = - float('inf')
    for i in set(arr):
        aux_arr = arr.copy()
        aux_arr.remove(i)
        sum_value = sum(aux_arr)

        # Update minimum and maximum
        if sum_value < minimum:
            minimum = sum_value
        if sum_value > maximum:
            maximum = sum_value
    print(f'{minimum} {maximum}')
