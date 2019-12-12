from listTailToRepresentStackTop import Stack
import math


def convert_decimal_to_binary(decimal):
    division_flag = True
    binary_stack = Stack()
    last_decimal = decimal

    while division_flag:
        quotient = math.floor(last_decimal / 2)
        remainder = last_decimal % 2
        binary_stack.push(remainder)
        last_decimal = quotient
        # 当商 < 进制数 时 不再做除法操作
        if quotient == 0:
            division_flag = False

    binary_str = ""
    for i in range(0, binary_stack.size(), 1):
        binary_str += str(binary_stack.pop())

    return binary_str


# print(convert_decimal_to_binary(233))


def divide_by_2(dec_number):
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        # // 在python中表示取整除
        dec_number = dec_number // 2

    bin_str = ""
    while not rem_stack.is_empty():
        bin_str += str(rem_stack.pop())

    return bin_str


print(divide_by_2(233))
