import time


def fib_recursive(n):
    if n <= 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# time.time() gives a floating point number which is the time in seconds
# since the start of the current "epoch" of the operating system, which
# is usually the start of 1970, but not taking into account leap seconds.
times = []
for i in range(20, 35):
    start1 = time.time()
    fib_recursive(i)
    end1 = time.time()
    elapsed1 = end1 - start1
    times.append(elapsed1)


for i in range(14):
    print(times[i+1]/times[i])
