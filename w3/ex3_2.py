def fibonacci_iter(n):
    if n <= 2:
        return 1
    ls = [1, 1]
    for i in range(n-2):
        ls.append(ls[-1] + ls[-2])
    return ls[-1]


for i in range(1, 100):
    print(f'the {i}th = {fibonacci_iter(i)}')
