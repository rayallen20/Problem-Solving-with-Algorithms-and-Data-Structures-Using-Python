"""
Queue类 使用list头部表示queue尾部 使用list尾部表示queue尾部
"""


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
