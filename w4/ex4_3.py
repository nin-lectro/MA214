from random import randint

# question (a)


def findXAndY(A):
    x = A[0]
    for i in A:
        if i != x:
            return x, i


def findXAndYRandom(A):
    x = A[randint(0, len(A) - 1)]
    new = x
    while(new == x):
        new = A[randint(0, len(A) - 1)]
    return x, new


def main():
    print(findXAndYRandom([3, 3, 3, 5, 5, 5]))


if __name__ == "__main__":
    main()
