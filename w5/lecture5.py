def countingSort(A, k):
    # n elements
    # all from range 0 ... k
    # O(n+k)
    count = [0 for i in range(k+1)]
    output = [0 for i in range(len(A))]
    # gets the counts
    for i in A:
        count[i] += 1

    # calculate the cumulative count
    for i in range(1, k+1):
        count[i] = count[i - 1] + count[i]

    # iterate over elements from the back
    # see where its cumulative count is
    # and place it into its correct place
    for i in reversed(A):
        output[count[i] - 1] = i
        count[i] -= 1

    return output


def radixSort(A, k, d):
    # assume n numbers which are all
    # d digits long
    # and each digit comes from 0 .... k
    # O(d*(n+k))
    pass


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
    a = [4, 2, 3, 6, 8, 10]
    print(countingSort(a, 10))


if __name__ == '__main__':
    main()
