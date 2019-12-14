import string
from listTailToRepresentStackTop import Stack

# TODO: 该函数边界条件判断虽然正确 但 可读性非常差 需要修改!


def convert_infix_to_epilogue(infix_string):
    infix_list = infix_string.split()
    # 存储操作符的栈
    operator_stack = Stack()

    # 优先级字典
    priority_dict = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }

    # 结果列表
    epilogue_list = []

    for opera_char in infix_list:
        if opera_char in string.ascii_uppercase:
            # 当前字符是操作数 直接追加到结果列表尾部
            epilogue_list.append(opera_char)
        elif opera_char == ')':
            # 当前字符是) 则栈内的元素一直弹出 直到弹出的元素为(为止 并将弹出的元素追加到结果列表中
            tmp_bool = True
            while tmp_bool:
                operator_in_stack = operator_stack.pop()
                if operator_in_stack != '(':
                    epilogue_list.append(operator_in_stack)
                else:
                    break
        else:
            # 当前字符是操作符
            if operator_stack.is_empty():
                operator_stack.push(opera_char)
            elif priority_dict[operator_stack.peek()] >= priority_dict[opera_char] and opera_char != '(':
                # 栈顶的操作符优先级高于或等于当前操作符 将栈内所有元素弹出并追加到结果列表中 然后将当前操作符压入栈内
                while not operator_stack.is_empty():
                    epilogue_list.append(operator_stack.pop())
                operator_stack.push(opera_char)
            else:
                # 栈顶的操作符优先级低于当前操作符 将当前操作符压入栈内
                operator_stack.push(opera_char)

    # 中序表达式遍历完毕 栈内还有操作符 则所有元素弹出并追加至结果列表中
    while not operator_stack.is_empty():
        epilogue_list.append(operator_stack.pop())

    return " ".join(epilogue_list)


print(convert_infix_to_epilogue(" ( A + B ) * ( C + D ) "))
print(convert_infix_to_epilogue(" ( A + B ) * C "))
print(convert_infix_to_epilogue("A + B * C"))
