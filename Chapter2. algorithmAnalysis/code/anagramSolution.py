import pysnooper

"""
遍历字符串A,检测是否每个字符均在字符串B内出现.
若在字符串A中出现不存在于字符串B的字符,则二者不是异序词关系.
"""


# @pysnooper.snoop(output="./log/debug_anagramSolution.log", prefix="--*--")
def my_anagram_solution1(s1, s2):
    is_anagram = True
    s1_chars = list(s1)
    s2_chars = list(s2)

    i = 0
    while i <= len(s1_chars) - 1:
        j = 0
        while j <= len(s2_chars) - 1:
            if s1_chars[i] == s2_chars[j]:
                # 若找到相同字符 则继续比较s1中的下一个字符
                break
            elif s1_chars[i] != s2_chars[j] and j != len(s2_chars) - 1:
                # 若没找到相同字符 则继续比较s2中的下一个字符
                j += 1
            elif j == len(s2_chars) - 1:
                # 若遍历了所有s2中的字符 没有出现和s1中的字符相同的字符
                is_anagram = False
                return is_anagram
        i += 1

    return is_anagram


# print(my_anagram_solution1("aaa", "bbb"))
# print(my_anagram_solution1("python", "typhon"))
# print(my_anagram_solution1("earth", "heart"))

"""
遍历字符串A,检测是否每个字符均在字符串B内出现
若出现,则将字符串B内相同的字符替换为None
"""


def book_anagram_solution1(s1, s2):
    a_list = list(s2)
    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            a_list[pos2] = None
        else:
            still_ok = False

        pos1 += 1

    return still_ok


# print(book_anagram_solution1("aaa", "bbb"))
# print(book_anagram_solution1("python", "typhon"))
# print(book_anagram_solution1("earth", "heart"))

"""
分别将字符串A和字符串B排序 比对排序后的结果是否相同
"""


# @pysnooper.snoop(output="./log/debug_anagramSolution.log", prefix="--*--")
def my_anagram_solution2(s1, s2):
    s1_chars = list(s1)
    s2_chars = list(s2)

    s1_chars.sort()
    s2_chars.sort()

    if s1_chars == s2_chars:
        return True
    else:
        return False


# print(my_anagram_solution2("aaa", "bbb"))
# print(my_anagram_solution2("python", "typhon"))
# print(my_anagram_solution2("earth", "heart"))

"""
分别将字符串A和字符串B排序 排序后比对2个列表在同一个位置上的元素值是否相同
"""


def book_anagram_solution2(s1, s2):
    a_list = list(s1)
    b_list = list(s2)

    a_list.sort()
    b_list.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list[pos] == b_list[pos]:
            pos += 1
        else:
            matches = False
            return matches

    return matches


# print(my_anagram_solution2("aaa", "bbb"))
# print(my_anagram_solution2("python", "typhon"))
# print(my_anagram_solution2("earth", "heart"))

"""
检测字符串A和字符串B中每个字符出现的次数
如果每个字符均出现2次 则为异序词
否则不是异序词
"""


def my_anagram_solution3(s1, s2):
    calc_dict = {}
    for s1_char in s1:
        if calc_dict.get(s1_char) is None:
            calc_dict[s1_char] = 1
        else:
            calc_dict[s1_char] += 1

    for s2_char in s2:
        if calc_dict.get(s2_char) is None:
            calc_dict[s2_char] = 1
        else:
            calc_dict[s2_char] += 1

    for char in calc_dict:
        if calc_dict[char] % 2 != 0:
            return False

    return True


# print(my_anagram_solution3("aaa", "bbb"))
# print(my_anagram_solution3("python", "typhon"))
# print(my_anagram_solution3("earth", "heart"))


"""
遍历2个字符串 
以每个字符串中的每个字符的ASCII码为list中的索引
以每个字符串中的每个字符出现的次数为值 存储每个字符出现的次数
最终比对2个list同一个索引上的值是否相等 
"""


def book_anagram_solution3(s1, s2):
    calc_list_a = [0] * 26
    calc_list_b = [0] * 26

    for i in range(len(s1)):
        # ord():接收一个字符 返回该字符的ASCII码或Unicode码
        pos = ord(s1[i]) - ord('a')
        calc_list_a[pos] = calc_list_a[pos] + 1

    for j in range(len(s2)):
        pos = ord(s2[j]) - ord('a')
        calc_list_b[pos] = calc_list_b[pos] + 1

    k = 0
    still_ok = True
    while k < 26 and still_ok:
        if calc_list_a[k] == calc_list_b[k]:
            k += 1
        else:
            still_ok = False

    return still_ok


print(book_anagram_solution3("aaa", "bbb"))
print(book_anagram_solution3("python", "typhon"))
print(book_anagram_solution3("earth", "heart"))
