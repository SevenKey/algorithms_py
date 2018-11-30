
#  反转链表
class ReversalLinkedList():
    def __init__(self):
        pass

    def reversal(self, head):
        pre, cur = None, head
        while cur is not None:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
