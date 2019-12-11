"""
逻辑门的基类 该类实现了:
    1. 接收输入
    2. 获取输入
    3. 获取输出
3个方法
"""


class LogicGate:
    """
    label: 门的名字
    output: 执行结果
    """

    def __init__(self, name):
        self.label = name
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        # perform v. 执行
        self.output = self.perform_gate_logic()
        return self.output


"""
2个输入的逻辑门的基类
"""


class BinaryGate(LogicGate):
    def __init__(self, name):
        # pin: 引脚 计算机电路设计中对输入值的专有名词
        super().__init__(name)
        self.pinA = None
        self.pinB = None

    def get_pin_a(self):
        if self.pinA is None:
            return int(input("Enter Pin A input " + self.get_label() + "-->"))
        else:
            return self.pinA.get_from().get_output()

    def get_pin_b(self):
        if self.pinB is None:
            return int(input("Enter Pin B input " + self.get_label() + "-->"))
        else:
            return self.pinB.get_from().get_output()

    def set_next_pin(self, source):
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


"""
1个输入的逻辑门的基类
Unary: adj 一元的
"""


class UnaryGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input("Enter Pin input " + self.get_label() + "-->"))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PIN")


"""
与门 实现类 具体实现performGateLogic()的子类
"""


class AndGate(BinaryGate):
    def __init__(self, name):
        super().__init__(name)

    def perform_gate_logic(self):
        pin_a = self.get_pin_a()
        pin_b = self.get_pin_b()

        if pin_a == 1 and pin_b == 1:
            return 1
        else:
            return 0

    def get_output(self):
        super().get_output()
        print("%s output = %d" % (self.label, self.output))


"""
或门 实现类 具体实现performGateLogic()的子类
"""


class OrGate(BinaryGate):
    def __init__(self, name):
        super().__init__(name)

    def perform_gate_logic(self):
        pin_a = self.get_pin_a()
        pin_b = self.get_pin_b()

        if pin_a == 1 or pin_b == 1:
            return 1
        else:
            return 0

    def get_output(self):
        super().get_output()
        print("%s output = %d" % (self.label, self.output))


"""
非门 实现类 具体实现performGateLogic()的子类
"""


class NotGate(UnaryGate):
    def __init__(self, name):
        super().__init__(name)

    def perform_gate_logic(self):
        pin = self.get_pin()

        if pin == 1:
            return 0
        else:
            return 1

    def get_output(self):
        super().get_output()
        print("%s output = %d" % (self.label, self.output))


"""
连接器用于连接2个逻辑门
"""


class Connector:
    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate

        to_gate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")

c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

g4.get_output()
