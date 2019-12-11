import timeit


def test1():
    my_list = []
    for i in range(1000):
        my_list += [i]


def test2():
    my_list = []
    for i in range(1000):
        my_list.append(i)


def test3():
    my_list = [i for i in range(1000)]


def test4():
    my_list = list(range(1000))


t1 = timeit.Timer("test1()", "from __main__ import test1")
# concat n. 合并多个数组; 合并多个字符串
print("concat ", t1.timeit(1000), "milliseconds")

t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(1000), "milliseconds")

t3 = timeit.Timer("test3()", "from __main__ import test3")
# comprehension n. 理解; 包含
print("comprehension ", t3.timeit(1000), "milliseconds")

t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(1000), "milliseconds")
