from listHeadRepresentQueueHead import Queue


def pass_potato(players, pass_num):
    current_round_num = 0
    wait_queue = Queue()
    while True:
        while current_round_num < pass_num:
            if len(players) != 0:
                # 将送出土豆的玩家放入等待序列中
                wait_queue.enqueue(players.pop())
            else:
                # 将所有等待队列中的玩家放入游戏队列
                while not wait_queue.is_empty():
                    players.append(wait_queue.dequeue())
                # 游戏队列中的第1位玩家再次开始传递土豆
                wait_queue.enqueue(players.pop())
            current_round_num += 1

        while current_round_num == pass_num:
            # 到达传递次数 淘汰玩家
            if len(players) != 0:
                # 若此时游戏队列中还有玩家 则游戏队列中的第1位玩家被淘汰
                # 等待队列中的玩家被追加到游戏队列尾部
                eliminated = players.pop(0)
                while not wait_queue.is_empty():
                    players.append(wait_queue.dequeue())
            else:
                # 此时游戏队列中没有玩家 则等待队列中的第1位玩家被淘汰
                eliminated = wait_queue.dequeue()
                while not wait_queue.is_empty():
                    players.append(wait_queue.dequeue())

            print(eliminated)

            if len(players) == 1:
                return players


print(pass_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 19))
