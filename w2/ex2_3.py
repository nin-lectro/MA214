# my solution O(n)
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

# class solution O(nlgn)
def profit(A, start, end):
    if start == end:
        return 0
    mid = (start + end) // 2
    left = profit(A, start, mid)
    right = profit(A, mid + 1, end)

    cross = max(A[mid+ 1: end+1]) - min(A[start: mid + 1])
    return max(left, right, cross)

# class solution O(n)
def profit_iterate(A):
    cur_min = A[0]
    cur_profit = 0
    for price in A:
        if price < cur_min:
            cur_min = price
        else:
            cur_profit = max(cur_profit, price - cur_min)
    return cur_profit

def main():
    example = [10, 11, 7, 10, 6]
    print(f'Max profit is {profit_iterate(example)}')


if __name__ == '__main__':
    main()
