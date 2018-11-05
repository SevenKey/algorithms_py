import unittest
from cache import LRU


class TestCache(unittest.TestCase):

    def test_lru(self):
        node1 = LRU.LRULinkedNode(key=1, pre_node=None, next_node=None)
        node2 = LRU.LRULinkedNode(key=2, pre_node=None, next_node=None)
        node3 = LRU.LRULinkedNode(key=3, pre_node=None, next_node=None)
        node4 = LRU.LRULinkedNode(key=4, pre_node=None, next_node=None)
        node5 = LRU.LRULinkedNode(key=5, pre_node=None, next_node=None)
        node6 = LRU.LRULinkedNode(key=6, pre_node=None, next_node=None)

        lru = LRU.LRU()
        self.assertEqual(lru.get(1), None)
        lru.put(node=node1)
        self.assertEqual(lru.get(1), node1)
        lru.put(node=node2)
        lru.put(node=node3)
        lru.put(node=node4)
        lru.get(1)
        self.assertEqual(lru.get(1), node1)
        lru.put(node5)
        lru.put(node6)
        self.assertEqual(lru.get(2), node2)
