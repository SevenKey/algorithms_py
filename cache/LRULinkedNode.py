# lru 链表

class LRULinkedNode:
    __key__ = ""
    __pre_node__ = None
    __next_node__ = None

    def __int__(self, key, pre_node, next_node):
        self.__key__ = key
        self.__pre_node__ = pre_node
        self.__next_node__ = next_node

    def get_key(self):
        return self.__key__

    def get_pre_node(self):
        return self.__pre_node__

    def get_next_node(self):
        return self.__next_node__

    def set_pre_node(self, node):
        self.__pre_node__ = node

    def set_next_node(self, node):
        self.__next_node__ = node
