def countingSort(A):
    pass
    # pseudocode
    # n elements
    # all from range 0 ... k
    # iterate over elements
    # increase the count of each value
    # calculate the cumulative count
    # go backwards to insert it into the correct place
    # O(n+k)


def radixSort(A):
    pass
    # assume n numbers which are all
    # d digits long
    # and each digit comes from 0 .... k
    # then can iterate over each digit from the back
    # and stable sort based on the current digit
    # O(d*(n+k))


def bucketSort(A):
    # assume numbers come from a certain distribution
    # for example uniform distribution [0, 1)
    # Then split interval into n even buckets
    # Put each value into its correct bucket
    # Insertion sort the buckets
    # Join the buckets together
    buckets = [[] for i in range(len(A))]
    for num in A:
        buckets[int(num*len(A))].append(num)
    for bucket in buckets:
        insertion_sort(bucket)
    return [i for bucket in buckets for i in bucket]


def insertion_sort(A):
    for i in range(1, len(A)):
        current = A[i]
        j = i - 1
        while (j >= 0 and A[j] > current):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = current
    return A


def main():
    a = [0.32, 0.84, 0.12, 0.45, 0.93]
    print(bucketSort(a))


if __name__ == '__main__':
    main()
