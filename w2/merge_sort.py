def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    merged_list = []
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    merged_list += right[j:]
    merged_list += left[i:]
    return merged_list


print(merge_sort([3, 2, 5, 8, 1, 5, 2, 9]))
