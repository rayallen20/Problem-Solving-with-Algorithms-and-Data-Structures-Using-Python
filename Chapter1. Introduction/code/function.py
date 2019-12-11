def square(n):
    return n ** 2


def square_root(n):
    root = n / 2
    for k in range(20):
        root = (root + n / root) / 2

    return root


print(square_root(9))
print(square_root(4563))
