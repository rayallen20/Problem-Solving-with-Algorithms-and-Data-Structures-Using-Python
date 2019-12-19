from listHeadRepresentQueueTail import Queue
"""
红方实现:
    改良版传土豆:使用游戏序列的尾部作为等待序列
"""


def pass_potato(players, pass_num):
    current_round_num = 0
    players_queue = Queue()
    while len(players) != 0:
        players_queue.enqueue(players.pop(0))

    while players_queue.size() != 1:
        players_queue.enqueue(players_queue.dequeue())
        current_round_num += 1

        if current_round_num == pass_num:
            players_queue.dequeue()
            current_round_num = 0

    return players_queue.dequeue()


"""
蓝方实现
    改良版传土豆:使用游戏序列的尾部作为等待序列
    代码比对:
        从简洁性上看,蓝方胜
            蓝方使用计步器i作为记录本轮传递土豆的次数 到达次数则直接淘汰玩家
            红方使用变量记录本轮传递土豆次数 每当传递次数发生变化后 都要判断传递次数是否到达指定次数
            如使用计步器 则判断的代码实际上是可以省略的.
            
        从可读性上看,双方均势
            红方使用变量记录本轮传递次数,命名清晰,词可达意
            但蓝方虽然使用计步器记录本轮传递次数 但只要将i改为current_round_num 同样词可达意
            故可读性方面 双方均势            
"""


def hot_potato(name_list, num):
    player_queue = Queue()
    for name in name_list:
        player_queue.enqueue(name)

    while player_queue.size() > 1:
        for i in range(num):
            player_queue.enqueue(player_queue.dequeue())

        player_queue.dequeue()

    return player_queue.dequeue()


print(pass_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
