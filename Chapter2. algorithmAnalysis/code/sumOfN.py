import time


def sum_of_n(n):
    start = time.time()
    my_sum = 0
    for i in range(1, n + 1):
        my_sum += i

    end = time.time()

    return my_sum, end - start


def foo(tom):
    fred = 0
    for bill in range(1, tom + 1):
        fred += bill

    return fred


for j in range(5):
    print("Sum is %d required %10.7f seconds" % sum_of_n(1000000))


def new_sum_of_n(n):
    start = time.time()
    my_sum = (n * (n + 1)) / 2
    end = time.time()
    return my_sum, end - start


for k in range(5):
    print("New sum is %d required %10.7f seconds" % new_sum_of_n(1000000))
