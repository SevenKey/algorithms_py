# 计算一个数的阶乘连续尾号为0个数 个数如果过大对100007取余

class Factorial:

    def __init__(self):
        pass

    def continuousZeroCount(self, num):
        counts = 0
        while num / 5 > 0:
            counts = counts + int(num / 5)
            num = int(num / 5)

        return counts
