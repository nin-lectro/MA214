def find_max_profit(A):
    if len(A) == 1:
        return (A[0], A[0], 0)

    mid = len(A) // 2

    min_left, max_left, profit_left = find_max_profit(A[:mid])
    min_right, max_right, profit_right = find_max_profit(A[mid:])

    current_profit = max(profit_left, profit_right, max_right - min_left)

    current_min = min(min_left, min_right)
    current_max = max(max_left, max_right)

    return (current_min, current_max, current_profit)


def main():
    example = [3, 7, 2, 1, 3, 8, 5, 2]
    print(f'Max profit is {find_max_profit(example)[2]}')


if __name__ == '__main__':
    main()
