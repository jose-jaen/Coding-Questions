import re
from typing import List


def weighted_uniform_strings(s: str, queries: List[int]):
    results = []
    distribution = {}
    unique_letters = set(s)
    for letter in unique_letters:
        max_count = max(len(m) for m in re.findall(pattern=f'{letter}+', string=s))
        distribution[letter] = (ord(letter) - 96, max_count)
    for i in range(len(queries)):
        for letter in unique_letters:
            divisible = queries[i] % distribution[letter][0] == 0
            remainder = queries[i] / distribution[letter][0]
            if divisible and remainder <= distribution[letter][1]:
                results.append('Yes')
                break
        if len(results) < i + 1:
            results.append('No')
    return results
