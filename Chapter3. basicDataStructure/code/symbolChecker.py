from listTailToRepresentStackTop import Stack


def symbol_checker(par_string):
    checked_stack = Stack()

    is_balanced = True

    for i in range(0, len(par_string), 1):
        checked_char = par_string[i]
        if checked_char in "([{":
            checked_stack.push(checked_char)
        elif checked_char in ")]}":
            right_symbol = checked_stack.pop()
            if is_matches(right_symbol, checked_char):
                continue
            else:
                is_balanced = False
                return is_balanced

    return is_balanced


def is_matches(left_symbol, right_symbol):
    left_chars = "([{"
    right_chars = ")]}"
    return left_chars.index(left_symbol) == right_chars.index(right_symbol)


print(symbol_checker("[{()]"))
