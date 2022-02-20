from random import randint


def quicksort(A, start, end):
    if start < end:
        pivot = partition(A, start, end)
        quicksort(A, start, pivot - 1)
        quicksort(A, pivot + 1, end)


def partition(A, start, end):
    pivot_val = A[end]
    i = start - 1  # represents index of at least val below the pivot

    # j represents the index of correctly formatted indices
    for j in range(start, end):  # don't need to check last value
        if A[j] < pivot_val:
            # swap a[j] with a[i+1]
            A[j], A[i+1] = A[i+1], A[j]
            i += 1
    # swap the pivot into its correct place
    A[end], A[i+1] = A[i+1], A[end]
    return i + 1


def randomisedQuicksort(A, start, end):
    if start < end:
        # places a random digit at the end as the pivot
        new_pivot = randint(start, end)
        A[end], A[new_pivot] = A[new_pivot], A[end]

        pivot = partition(A, start, end)
        quicksort(A, start, pivot - 1)
        quicksort(A, pivot + 1, end)


def main():
    example = [9, 8, 3, 1, 5, 3, 2, 4]
    randomisedQuicksort(example, 0, len(example) - 1)
    print(example)


if __name__ == '__main__':
    main()
