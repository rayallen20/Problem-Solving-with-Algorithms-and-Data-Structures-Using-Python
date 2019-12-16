from listTailToRepresentStackTop import Stack

"""
红方实现:计算一个后序表达式的值
"""


def calc_postfix_expr(postfix_expr):
    postfix_expr = postfix_expr.split()

    # 保存操作数的栈
    operands = Stack()

    for i in range(0, len(postfix_expr), 1):
        token = postfix_expr[i]

        # 判断token是否为操作数
        try:
            token = float(token)
            is_operand = True
        except ValueError:
            is_operand = False

        if is_operand:
            # 操作数直接压入栈
            operands.push(token)
        else:
            # 操作符则需要从栈内弹出2个操作数
            # 先弹出的放在操作符的右边
            # 后弹出的放在操作符的左边
            operand_right, operand_left = operands.pop(), operands.pop()

            # 创建临时表达式并计算临时表达式的值
            tmp_value = eval(str(operand_left) + str(token) + str(operand_right))

            if i == len(postfix_expr) - 1:
                return tmp_value
            else:
                operands.push(tmp_value)


# print(calc_postfix_expr("4 5 6 * +"))
# print(calc_postfix_expr("7 8 + 3 2 + /"))

"""
蓝方实现:计算一个后序表达式的值
个人认为:
1. 这段代码从功能上来讲不如红方实现 因为下面这段代码支持的操作数范围仅有[0,9]
2. 但从可读性上有2个地方比红方强 1个地方不如我:
    优点
        1. 因为红方使用了eval()函数 很明显的降低了可读性
        2. 蓝方for range 直接遍历的是list中的元素 表现力强 之所以他可以这么做 
           是因为他在处理一个计算后的值时,直接压入栈内 等到遍历结束后 也直接从栈内弹出元素并返回
           这就意味着:在遍历时 不需要考虑当前遍历的元素是否是list内的最后一个元素
           换言之 表现力强只是结果 其过程是优化了边界条件的判断
    缺点:
        1. 红方在从栈内取出操作数时 使用 1 2作为操作数变量的命名 是大忌 
           尤其是在处理这种有顺序的操作时 更不能使用这种命名
           
eval: addr 评估 评价 (解释为评价时 等价于evaluation)
"""


def postfix_eval(postfix_expr):
    operand_stack = Stack()

    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(float(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)

    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
