# 反转链表
class ReversalLinkedList():
    def __init__(self):
        pass

    def reversal(self, head):
        pre, cur = None, head
        while cur is not None:
            cur.next, pre, cur = pre, cur, cur.next
        return pre




current = head
while current is not None:
    print(current.x)
    current = current.next

reversed = ReversalLinkedList()
tail = reversed.reversal(head)

current = tail
while current is not None:
    print(current.x)
    current = current.next
