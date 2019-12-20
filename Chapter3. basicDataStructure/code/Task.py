import random


class Task:
    """
    构造方法:初始化任务时需设定任务被创建的时间戳
    初始化时Task内部将设置任务所要打印的页数
    """

    def __init__(self, timestamp):
        self.create_task_time = timestamp
        self.pages = random.randrange(1, 21)

    def get_create_task_time(self):
        return self.create_task_time

    def get_pages(self):
        return self.pages

    """
    本方法负责计算任务在队列中等待的时间 参数current_time的含义为任务从队列中出列
    进入打印机那一时刻的时间戳
    """

    def wait_time(self, current_time):
        return current_time - self.create_task_time
