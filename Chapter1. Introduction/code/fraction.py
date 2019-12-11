class Fraction:
    """
    top 分子的值
    bottom 分母的值
    num: 分子字段
    den: 分母字段
    """

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    """
    该方法用于打印
    """

    def show(self):
        print("%d/%d" % (self.num, self.den))

    """
    该方法用于覆写内置的__str__方法 __str__ = PHP中的toString()
    """

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    """
    该方法用于覆写内置的__add__方法 使其支持操作符+
    该操作符表示的含义为:2个分数相加
    """

    def __add__(self, other_fraction):
        # # step1. self的分子 * other的分母
        # self.num *= other.den
        #
        # # step2. other的分子 * self的分母
        # other.num *= self.den
        #
        # # step3. 求分子的和
        # self.num += other.num
        #
        # # step4. self的分母 * other的分母
        # self.den *= other.den

        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        new_den = self.den * other_fraction.den

        common = gcd(new_num, new_den)

        # //在python中表示整数除法
        return Fraction(new_num // common, new_den // common)

    """
    __eq__方法相当于用于对象比较的 == 操作符
    python内置的对象比较只有在2个对象类型的变量指向同样的引用时 才会返回true
    但是实际上业务需要是:2个分数表示相同的小数 即可认为2个Fraction对象相等
    """
    
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum


"""
根据欧几里得算法:
a. 若m能够被n整除 则m与n的最大公因数为n
b. 若m不能被n整除 则m与n的最大公因数为n 与 (m % n)的最大公因数

实现思路:
    若 m % n == 0 return n
    若 m % n != 0
        step1. 将n保存在临时变量中
        step2. 计算新的n: n = m % n
        step3. m = 临时变量
"""


def gcd(m, n):
    while m % n != 0:
        newm = n
        newn = m % n

        m = newm
        n = newn
    return n


x = gcd(6, 8)
print(x)

myFraction = Fraction(3, 5)
myFraction.show()

myF = Fraction(3, 5)
print("I ate", myF, "of the pizza")

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)

print(f1 + f2)

f3 = Fraction(3, 4)
f4 = Fraction(3, 4)
print(f3 == f4)
