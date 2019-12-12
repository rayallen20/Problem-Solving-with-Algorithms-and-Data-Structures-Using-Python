class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if not self.items:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)
        return

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return IndexError("IndexError: pop from empty stack")

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[self.size() - 1]
        else:
            return IndexError("IndexError: stack index out of range")


# list_tail_represent_stack = Stack()
# print(list_tail_represent_stack.is_empty())
#
# list_tail_represent_stack.push(4)
# print(list_tail_represent_stack.items)
#
# list_tail_represent_stack.push('dog')
# print(list_tail_represent_stack.items)
#
# print(list_tail_represent_stack.peek())
#
# list_tail_represent_stack.push(True)
# print(list_tail_represent_stack.items)
#
# print(list_tail_represent_stack.size())
#
# print(list_tail_represent_stack.is_empty())
#
# list_tail_represent_stack.push(8.4)
# print(list_tail_represent_stack.items)
#
# list_tail_represent_stack.pop()
# print(list_tail_represent_stack.items)
#
# list_tail_represent_stack.pop()
# print(list_tail_represent_stack.items)
#
# print(list_tail_represent_stack.size())
