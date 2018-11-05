# 缓存淘汰算法 lru 最近最少使用

class LRUHeadNode:
    __tail__ = None
    __next_node__ = None
    __count__ = 0

    def __init__(self, next_node, tail):
        self.__tail__ = tail
        self.__next_node__ = next_node
        self.__count__ = 0

    def get_tail(self):
        return self.__tail__

    def set_tail(self, tail):
        self.__tail__ = tail

    def get_next_node(self):
        return self.__next_node__

    def set_next_node(self, node):
        self.__next_node__ = node

    def get_count(self):
        return self.__count__

    def increment_count(self):
        self.__count__ += 1


class LRULinkedNode:
    __key__ = ""
    __pre_node__ = None
    __next_node__ = None

    def __init__(self, key, pre_node, next_node):
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


class LRU:
    __MAX_COUNT__ = 5
    __head__ = LRUHeadNode(next_node=None, tail=None)

    def get_head(self):
        return self.__head__

    def __init__(self):
        pass

    def get(self, key):
        if (self.get_head().get_next_node() is None):
            return None
        node = self.get_head().get_next_node()
        while (None is not node):
            if key == node.get_key():
                self.move_to_head(node)
                return node
            else:
                node = node.get_next_node()
        return None

    def put(self, node):
        old_node = self.get_head().get_next_node()
        while (None is not old_node):
            if old_node.get_key() == node.get_key():
                self.move_to_head(old_node)
                break
            else:
                old_node = old_node.get_next_node()
        if self.get_head().get_count() >= self.__MAX_COUNT__:
            self.lru_remove()
        self.insert_to_head(node)

    def insert_to_head(self, node):
        if self.get_head().get_next_node() is None:
            self.get_head().set_next_node(node)
            self.get_head().set_tail(node)
            node.set_pre_node(self.get_head)
            node.set_next_node(None)
        else:
            next_head_node = self.get_head().get_next_node()
            self.get_head().set_next_node(node)
            node.set_pre_node(self.get_head())
            node.set_next_node(next_head_node)
            next_head_node.set_pre_node(node)

    def move_to_head(self, node):
        if self.get_head().get_count() <= 2:
            return
        if self.get_head().get_tail() == node:
            self.get_head().set_tail(node.get_pre_node())
            tail = self.get_head().get_tail()
            tail.set_next_node(None)
        self.insert_to_head(node)

    def lru_remove(self):
        tail = self.get_head().get_tail()
        node = tail.get_pre_node()
        self.get_head().set_tail(node)
        node.set_next_node(None)



