def medianPartition(A, start, end):
    # find median
    mid = (start + end) // 2
    if A[start] <= A[mid] <= A[end] or A[start] >= A[mid] >= A[end]:
        A[end], A[mid] = A[mid], A[end]
    elif A[mid] <= A[start] <= A[end] or A[mid] >= A[start] >= A[end]:
        A[start], A[mid] = A[start], A[end]
    # else end is median

    i = start - 1
    for j in range(start, end):
        if A[j] <= A[end]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[end], A[i+1] = A[i+1], A[end]
    return i+1


def quicksort(A, start, end):
    if start < end:
        pivot = medianPartition(A, start, end)
        quicksort(A, start, pivot - 1)
        quicksort(A, pivot + 1, end)


def main():
    example = [9, 4, 3, 3, 6, 2345, 4]
    quicksort(example, 0, len(example) - 1)
    print(example)


if __name__ == '__main__':
    main()
