import timeit
import random

for i in range(10000, 100001, 10000):
    list_time_test = timeit.Timer("random.randrange(%d) in test_list" % i, "from __main__ import random, test_list")
    test_list = list(range(i))
    list_time = list_time_test.timeit(number=1000)

    dict_time_test = timeit.Timer("random.randrange(%d) in test_dict" % i, "from __main__ import random, test_dict")
    test_dict = {j: None for j in range(i)}
    dict_time = dict_time_test.timeit(number=1000)
    print("length = %d" % i)
    print("contain opera of list cost: %.5f" % list_time)
    print("contain opera of dict cost: %.5f" % dict_time)
    print("----------------------------")
