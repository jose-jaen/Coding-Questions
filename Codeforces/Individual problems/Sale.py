n, m = [int(i) for i in input().split()]
prices = sorted([abs(int(j)) for j in input().split() if int(j) <= 0], reverse=True)
res = prices[:m] if len(prices) >= m else prices
print(sum(res))
