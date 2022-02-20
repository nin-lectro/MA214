def recurseBinarySearch(A, start, end, x):
    if start > end:
        return None

    mid = (start + end) // 2
    if A[mid] == x:
        return mid
    elif A[mid] > x:
        return recurseBinarySearch(A, start, mid - 1, x)
    elif A[mid] < x:
        return recurseBinarySearch(A, mid + 1, end, x)


def iterativeBinarySearch(A, x):
    i = 0
    j = len(A) - 1
    while i <= j:
        mid = (i + j) // 2
        if A[mid] == x:
            return mid
        elif A[mid] > x:
            j = mid - 1
        elif A[mid] < x:
            i = mid + 1
    return None


print(iterativeBinarySearch([1, 3, 5, 7, 9, 9, 11, 13], 13))
