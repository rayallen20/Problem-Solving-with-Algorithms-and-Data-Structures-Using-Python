from listTailToRepresentStackTop import Stack


def par_checker(par_string):
    checked_stack = Stack()
    is_balanced = True
    for i in range(0, len(par_string), 1):
        checked_char = par_string[i]
        if checked_char == '(':
            checked_stack.push(checked_char)
        elif checked_char == ')':
            checked_stack.pop()

    if checked_stack.is_empty():
        return is_balanced
    else:
        print(checked_stack.items)
        is_balanced = False
        return is_balanced


print(par_checker("(()()()())"))
