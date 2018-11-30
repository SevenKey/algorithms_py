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


head = LinkedNode(0)
node1 = LinkedNode(1)
node2 = LinkedNode(2)
node3 = LinkedNode(3)
node4 = LinkedNode(4)
node5 = LinkedNode(5)
node6 = LinkedNode(6)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

current = head
while current is not None:
    print(current.x)
    current = current.next

reversed = ReversalTwoLinkedList()
tail = reversed.reversal(head)

current = tail
while current is not None:
    print(current.x)
    current = current.next
