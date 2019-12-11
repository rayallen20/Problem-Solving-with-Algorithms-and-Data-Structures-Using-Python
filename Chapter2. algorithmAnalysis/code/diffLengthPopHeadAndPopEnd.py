import timeit

pop_zero = timeit.Timer("zero_list.pop(0)", "from __main__ import zero_list")
pop_end = timeit.Timer("end_list.pop()", "from __main__ import end_list")

for i in range(1000000, 100000001, 1000000):
    print("len(list) = %d" % i)
    print("pop(0), pop()")
    zero_list = list(range(i))
    run_pop_zero = pop_zero.timeit(number=1000)

    end_list = list(range(i))
    run_pop_end = pop_end.timeit(number=1000)
    print("%.5f, %.5f" % (run_pop_zero, run_pop_end))
    print("-------------------------")
