import timeit

pop_zero = timeit.Timer("pop_zero_list.pop(0)", "from __main__ import pop_zero_list")
pop_zero_list = list(range(2000000))
print("pop(0) 1000 times cost: %15.5f ms" % pop_zero.timeit(number=1000))

pop_end = timeit.Timer("pop_end_list.pop()", "from __main__ import pop_end_list")
pop_end_list = list(range(2000000))
print("pop() 1000 times cost: %15.5f ms" % pop_end.timeit(number=1000))
