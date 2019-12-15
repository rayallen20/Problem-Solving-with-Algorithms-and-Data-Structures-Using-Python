import string
from listTailToRepresentStackTop import Stack


def convert_infix_to_epilogue(infix):
    infix = infix.split()

    # 优先级字典
    priority = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }

    # 暂存操作符的栈
    operators = Stack()

    # 后序表达式字符列表
    epilogue = []

    for char in infix:
        if char in string.ascii_uppercase:
            # 操作数直接追加至后续表达式列表结尾
            epilogue.append(char)
        else:
            if char == '(':
                # ( 直接压入栈内
                operators.push(char)
            elif char == ')':
                # ) 从栈内弹出元素 直到弹出的元素为(为止 并将这些弹出的操作符追加到结果列表中
                while True:
                    operator = operators.pop()
                    if operator != '(':
                        epilogue.append(operator)
                    break
            elif operators.is_empty():
                # 栈为空 则将当前运算符直接压入栈内
                operators.push(char)
            else:
                if priority[operators.peek()] < priority[char]:
                    # 栈不为空 且栈顶操作符的优先级低于当前操作符 直接将当前操作符压入栈内
                    operators.push(char)
                else:
                    # 栈不为空 且栈顶操作符的优先级高于或等于当前运算符
                    # 先将栈内所有运算优先级高于或等于当前运算符的运算符弹出 追加到结果列表尾部
                    # 再将当前运算符压入栈内
                    if priority[operators.peek()] >= priority[char]:
                        epilogue.append(operators.pop())
                    else:
                        operators.push(char)

    # 遍历结束 如栈内还有操作符 则弹出并追加到结果列表尾部
    while not operators.is_empty():
        operator = operators.pop()
        if operator != '(':
            epilogue.append(operator)

    return " ".join(epilogue)


print(convert_infix_to_epilogue(" ( A + B ) * ( C + D ) "))
print(convert_infix_to_epilogue(" ( A + B ) * C "))
print(convert_infix_to_epilogue("A + B * C"))
