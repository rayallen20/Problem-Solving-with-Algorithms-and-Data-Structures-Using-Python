from listHeadRepresentQueueTail import Queue
from Printer import Printer
from Task import Task
import random


def mock_lab_print(num_seconds, pages_per_minute):
    """
    :param num_seconds int 表示要模拟的时长 以秒为单位 例如 要模拟1小时 则该参数值为3600
    :param pages_per_minute int 表示打印机的速度 单位为页数/分钟
    """
    # 初始化打印机
    printer = Printer(pages_per_minute)

    # 初始化任务队列
    tasks = Queue()

    # 等待时间列表
    wait_times = []

    for current_timestamp in range(num_seconds):
        if is_new_task():
            # 创建任务 以当前的计步器值为任务的创建时刻
            task = Task(current_timestamp)
            tasks.enqueue(task)

        if (not printer.is_busy()) and (not tasks.is_empty()):
            # 取出下一个任务
            next_task = tasks.dequeue()
            # 以下一个任务进入打印机的时刻为任务开始被执行的时刻
            wait_times.append(next_task.wait_time(current_timestamp))
            # 打印机开始下一个任务
            printer.start_next(next_task)

        # 打印机开始工作
        printer.tick()

    average_wait_time = sum(wait_times) / len(wait_times)
    print("Average Wait %6.2f secs %3d tasks finished." % (average_wait_time, tasks.size()))


def is_new_task():
    probability = random.randrange(1, 181)
    if probability == 180:
        return True
    else:
        return False


for i in range(10):
    mock_lab_print(3600, 5)
