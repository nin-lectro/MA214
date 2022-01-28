def insertion_sort(A):
    for i in range(1, len(A)):
        current = A[i]
        j = i - 1
        while (j >= 0 and A[j] > current):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = current
    return A


print(insertion_sort([4, 3, 5, 8, 7, 1]))
