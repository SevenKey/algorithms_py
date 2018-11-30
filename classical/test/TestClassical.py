import unittest
from classical import Dijkstra, ReversalLinkedList, LinkedNode


class TestClassical(unittest.TestCase):

    def test_dijkstra(self):
        maps = dict()

        maps[1] = dict()
        maps[1][2] = 3
        maps[1][3] = 7

        maps[2] = dict()
        maps[2][3] = 1
        maps[2][4] = 1

        maps[3] = dict()
        maps[3][4] = 6

        maps[4] = dict()
        maps[4][5] = 2

        start = 2
        end = 5
        dijkstra = Dijkstra.Dijkstra()
        parents = dijkstra.get_closest_path(nodes=maps, start=start, end=end)
        node_list = list()
        temp = end
        while (temp != start):
            for node in parents.keys():
                if (node == temp):
                    node_list.append(node)
                    temp = parents[node]
        node_list.append(start)
        node_list.reverse()
        true_list = [2, 4, 5]
        self.assertListEqual(node_list, true_list)

    @staticmethod
    def build_linked_list():
        head = LinkedNode.LinkedNode(0)
        node1 = LinkedNode.LinkedNode(1)
        node2 = LinkedNode.LinkedNode(2)
        node3 = LinkedNode.LinkedNode(3)
        node4 = LinkedNode.LinkedNode(4)
        node5 = LinkedNode.LinkedNode(5)
        node6 = LinkedNode.LinkedNode(6)
        head.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6

        return head

    @staticmethod
    def get_linked_list_values(head):
        cur = head
        listValues = list()
        while cur is not None:
            listValues.append(cur.x)
            cur = cur.next
        return listValues

    def test_reversal(self):
        head = TestClassical.build_linked_list()
        list1 = TestClassical.get_linked_list_values(head)
        reversed = ReversalLinkedList.ReversalLinkedList()
        tail = reversed.reversal(head)
        list2 = TestClassical.get_linked_list_values(tail)
        list2.reverse()
        self.assertListEqual(list1,list2)


if __name__ == '__main__':
    unittest.main()
