from node import Node


class UnorderedList:
    def __init__(self):
        """
        构造方法 初始化时设置UnorderedList头部为空 标识初始化后的UnorderedList实例为空
        :return: void
        """
        self.head = None

    def is_empty(self):
        """
        本方法用于检测UnorderedList的实例是否为空
        实际上这里的是否为空指的是一个逻辑上的"空" 因为一个对象不存在空的概念
        :return: void
        """
        return self.head is None

    def add(self, item):
        """
        本方法用于添加新节点至列表头部
        :param item:mixed
        :return: void
        """
        head_node = Node(item)
        head_node.set_next(self.head)
        self.head = head_node

    def length(self):
        """
        本方法用于统计UnorderedList的长度
        :return: count int
        """
        current_ref = self.head
        count = 0
        while current_ref is not None:
            count += 1
            current_ref = current_ref.get_next()
        return count

    def search(self, item):
        """
        本方法用于检测给定值是否存在于UnorderedList中
        :param item:mixed 待搜索值
        :return: bool True表示待搜索值存在于列表中 False则反之
        """
        current_ref = self.head
        while current_ref is not None:
            if current_ref.get_data() == item:
                return True
            else:
                current_ref = current_ref.get_next()

        return False


test_linked_list = UnorderedList()
test_linked_list.add(31)
test_linked_list.add(77)
test_linked_list.add(17)
test_linked_list.add(93)
test_linked_list.add(26)
test_linked_list.add(54)
test_linked_list.add(93)

# print(test_linked_list.head.next.data)
# print(test_linked_list.length())
# print(test_linked_list.search(93))
