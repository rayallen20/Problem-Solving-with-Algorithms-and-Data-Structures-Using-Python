class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if not self.items:
            return True
        else:
            return False

    def push(self, item):
        self.items.insert(0, item)
        return

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return IndexError("IndexError: stack from empty list")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return IndexError("IndexError: stack index out of range")

    def size(self):
        return len(self.items)


list_head_represent_stack = Stack()
print(list_head_represent_stack.is_empty())

list_head_represent_stack.push(4)
print(list_head_represent_stack.items)

list_head_represent_stack.push('dog')
print(list_head_represent_stack.items)

print(list_head_represent_stack.peek())

list_head_represent_stack.push(True)
print(list_head_represent_stack.items)

print(list_head_represent_stack.size())

print(list_head_represent_stack.is_empty())

list_head_represent_stack.push(8.4)
print(list_head_represent_stack.items)

list_head_represent_stack.pop()
print(list_head_represent_stack.items)

list_head_represent_stack.pop()
print(list_head_represent_stack.items)

print(list_head_represent_stack.size())
