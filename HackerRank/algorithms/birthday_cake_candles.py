from typing import List


def birthday_cake_candles(candles: List[int]) -> int:
    maximum = max(candles)
    return candles.count(maximum)
