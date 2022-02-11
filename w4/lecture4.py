def quicksort(A, start, end):
    pivot = partition(A, start, end)
    quicksort(A, start, pivot)
    quicksort(A, pivot + 1, end + 1)


def partition(A, start, end):
    A
