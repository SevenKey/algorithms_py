class LinkedListLoop():

    def __init__(self):
        pass

    def hasLoop1(self, head):
        cur = head
        history = set()
        while cur is not None:
            if cur.x in history:
                return True
            history.add(cur.x)
            cur = cur.next
        return False

    def hasLoop2(self, head):
        fast, low = head, head
        while low and fast:
            low = low.next
            if fast.next and fast.next.next:
                return False
            fast = fast.next.next
            if low == fast:
                return True
        return False
