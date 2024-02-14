def staircase(n: int) -> None:
    # Write your code here
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)
