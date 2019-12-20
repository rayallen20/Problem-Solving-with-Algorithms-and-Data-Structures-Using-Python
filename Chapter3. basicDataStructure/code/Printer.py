class Printer:
    """
    构造方法:初始化打印机时需设定打印速度 打印速度的单位为: 页数/分钟
    初始化时Printer内部将设定无当前正在进行的任务 且 当前任务所需时间为0
    任务所需时间单位为:分钟
    """

    def __init__(self, pages_per_minute):
        self.print_speed = pages_per_minute
        self.current_task = None
        self.time_cost = 0

    """
    本方法负责以1秒/调用次数 的速度,减少当前任务所需时间
    若当前任务所需时间为0 则表示打印机中当前正在处理的任务结束了
    打印机又回到了等待执行任务的状态
    """

    def tick(self):
        if self.current_task is not None:
            self.time_cost -= 1
            if self.time_cost <= 0:
                self.current_task = None

    """
    本方法负责判断打印机当前的状态 若当前存在正在处理的任务 则打印机为繁忙状态
    否则 打印机为空闲状态
    """

    def is_busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    """
    本方法负责开始下一个任务 将下一个任务 以及下一个任务所需时间赋值到本类的
    current_task和time_cost字段上
    所需时间 = 任务打印页数 * 60 / 打印速度 其中 60为 分钟/小时 所需时间单位为:分钟
    """

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_cost = new_task.get_pages() * 60 / self.print_speed
