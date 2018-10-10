# 缓存淘汰算法 lru 最近最少使用
from cache import LRULinkedNode


class LRU:

    def __int__(self):
        self.__dict_cache__ = dict()

        self.__linked_head__ = dict()
        self.__linked_head__["tail"] = None
        self.__linked_head__["size"] = 0
        self.__linked_head__["next_node"] = None

    def get(self, key):
        node = self.__dict_cache__.get(key)
        if (None is node):
            return node

        linked_node = node.get("node")
        pre_node = linked_node.get_pre_node()
        next_node = linked_node.get_next_node()

        if (self.__linked_head__.get("tail") is linked_node):
            self.__linked_head__["tail"] = pre_node

        pre_node.set_next_node(node=next_node)
        next_node.set_pre_node(node=pre_node)
        linked_node.set_pre_node(node=self.__linked_head__)
        linked_node.set_next_node(node=self.__linked_head__.get("next_node"))

        return node.get("value")

    def put(self, key, value):
        node = self.__dict_cache__.get(key)
        if (None is not node):
            node["value"] = value
            return None

        if (self.__linked_head__.get("size") >= 10):
            remove_node = self.__linked_head__.get("tail")
            remove_key = remove_node.get_key()

            del self.__dict_cache__[remove_key]
            self.__linked_head__["tail"] = remove_node.get_pre_node()
            remove_node.set_pre_node(node=None)

        node = LRULinkedNode.LRULinkedNode(key=key, pre_node=self.__linked_head__,
                                           next_node=self.__linked_head__.get("next_node"))
        dict_value = dict()
        dict_value["value"] = value
        dict_value["node"] = node
        self.__dict_cache__[key] = dict_value
