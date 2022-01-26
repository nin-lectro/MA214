def peak_iter(arr):
    for i, value in enumerate(arr):
        if i == 0 and value > arr[1]:
            return i
        elif i == len(arr) - 1:
            return i
        elif value > arr[i - 1] and value > arr[i + 1]:
            return i


def main():
    example1 = [1, 2, 3, 4, 5, 6, 7, 8]
    example2 = [8, 7, 6, 5, 4, 3, 2, 1]
    example3 = [1, 2, 3, 4, 3, 2, 1, 0]
    ls = [example1, example2, example3]
    for l in ls:
        print(f"Peak in {l} is at index: {peak_iter(l)}")


if __name__ == '__main__':
    main()
