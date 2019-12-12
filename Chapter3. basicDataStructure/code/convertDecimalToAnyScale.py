from listTailToRepresentStackTop import Stack


def convert_decimal_to_any_scale(decimal, scale_num):
    scale_stack = Stack()
    num_chars = "0123456789ABCDEF"

    while decimal > 0:
        remainder = decimal % scale_num
        scale_stack.push(remainder)
        decimal = decimal // scale_num

    scale_str = ""

    while not scale_stack.is_empty():
        scale_str += num_chars[scale_stack.pop()]

    return scale_str


print(convert_decimal_to_any_scale(233, 16))
