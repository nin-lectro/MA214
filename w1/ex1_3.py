def peak_divide_conquer(arr, i, j):
    mid = (i + j) // 2
    # base case
    if i == j:
        return i
    # check for peak
    if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        return mid
    # need to go to right
    elif arr[mid] > arr[mid - 1]:
        return peak_divide_conquer(arr, mid + 1, j)
    # need to go to left
    else:
        return peak_divide_conquer(arr, i, mid - 1)


def main():
    example1 = [1, 2, 3, 4, 5, 6, 7, 8]
    example2 = [8, 7, 6, 5, 4, 3, 2, 1]
    example3 = [1, 2, 3, 4, 3, 2, 1, 0]
    ls = [example1, example2, example3]
    for l in ls:
        print(f"Peak in {l} is at index: {peak_divide_conquer(l, 0, 7)}")


if __name__ == '__main__':
    main()
