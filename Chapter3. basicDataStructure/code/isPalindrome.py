import math
from listHeadRepresentDequeRear import Deque


def is_palindrome_by_char(pending_detection):
    half_len = math.floor(len(pending_detection) / 2)
    for i in range(half_len):
        if pending_detection[i] != pending_detection[len(pending_detection) - 1 - i]:
            return False

    return True


def is_palindrome_by_deque(pending_detection):
    deque = Deque()

    # 将字符串中的字符在双端队列的队尾添加
    for char in pending_detection:
        deque.add_rear(char)

    # 从双端队列左右两侧同时取字符 比对是否相同
    while deque.size() > 1:
        # 原字符串中 左侧的字符在双端队列的前端 右侧的字符在双端队列的后端
        left_char, right_char = deque.remove_front(), deque.remove_rear()
        if left_char != right_char:
            return False

    return True


print(is_palindrome_by_deque("abcba"))
print(is_palindrome_by_deque("radar"))
print(is_palindrome_by_deque("toot"))
print(is_palindrome_by_deque("madam"))
print(is_palindrome_by_deque("aabbcc"))