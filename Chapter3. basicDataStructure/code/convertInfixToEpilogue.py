import string
from listTailToRepresentStackTop import Stack

"""
中序表达式转化为后续表达式 红方实现
"""


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
                operator = operators.pop()
                while operator != '(':
                    epilogue.append(operator)
                    operator = operators.pop()
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
    # 因为遍历已经结束了 所以必然在栈内不会有( 因此不用判断
    while not operators.is_empty():
        # print(operators.items)
        epilogue.append(operators.pop())

    return " ".join(epilogue)


print(convert_infix_to_epilogue(" ( A + B ) * ( C + D ) "))
print(convert_infix_to_epilogue(" ( A + B ) * C "))
print(convert_infix_to_epilogue("A + B * C"))


"""
中序表达式转化为后续表达式 蓝方实现
蓝方代码和红方代码比对 得出为什么蓝方代码比红方代码看上去更简洁且表达力更强
核心点在于:
    在检测到操作符时,红方的思路是:
        先检测栈是否为空
        再比对操作符优先级
    蓝方的思路是:
        当栈不为空时检测运算符优先级
    
因此看上去蓝方的代码量更少 且蓝方用词精确 故 蓝方胜
"""


def infix_to_postfix(infix_expr):
    # prec: addr 优先级 (等于precedence)
    prec = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }

    op_stack = Stack()
    postfix_list = []

    # token: n. 记号 符号 标记 (语言学中的专有释义)
    token_list = infix_expr.split()

    for token in token_list:
        if token in string.ascii_uppercase:
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            # 这一段比我那个 while True ... break 写的要精简
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)


print(infix_to_postfix(" ( A + B ) * ( C + D ) "))
print(infix_to_postfix(" ( A + B ) * C "))
print(infix_to_postfix("A + B * C"))
