# 反转链表
class LinkedNode():
    def __init__(self, x):
        self.x = x
        self.next = None


class ReversalTwoLinkedList():
    def __init__(self):
        pass

    def reversal(self, head):
        count = 0
        pre = None
        cur = head

        while cur and cur.next:
            a = cur
            b = a.next

            a.next = b.next
            b.next = a
            count += 1
            if count == 1:
                head = b
            else:
                pre.next = b
            pre = a
            cur = cur.next
        return head
