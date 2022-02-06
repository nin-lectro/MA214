# Implement heap sort
def maxHeapify(A, i, size):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # finds largest of the three
    for c in [left, right]:
        if c < size and A[c] > A[largest]:
            largest = c
    # checks if original was largest
    if largest == i:
        return

    A[i], A[largest] = A[largest], A[i]
    # keep heapify until down
    maxHeapify(A, largest, size)


def buildMaxHeap(A):
    # as A[len(A)//2] ... A[len(A) - 1] are leaves
    # specifically ceil(n/2) are leaves
    i = len(A)//2 - 1
    size = len(A)
    while i >= 0:
        maxHeapify(A, i, size)
        i -= 1


def heapSort(A):
    buildMaxHeap(A)
    size = len(A)

    # keeps swapping last and first element and running max heapify
    while size > 1:
        A[0], A[size - 1] = A[size - 1], A[0]
        size -= 1
        maxHeapify(A, 0, size)


example = [2, 3, 1]
heapSort(example)
print(example)
