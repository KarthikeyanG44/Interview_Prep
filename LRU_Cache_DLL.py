"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity. Both the operations must be done in O(1) time
"""


##### LRU Cache Implementation using Doubly Linked List #####
class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = None
        self.tail = None

    ####### Call this method only only if you are moving nodes exisiting in the DLL ########
    def move_node_front(self, node):
        if node == self.head:
            return
        elif node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node

    def get(self, key: int) -> int:
        if key in self.cache:
            corresponding_node = self.cache[key]
            self.move_node_front(corresponding_node)
            return corresponding_node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if not self.cache:
            self.cache[key] = Node(key, value)
            self.head = self.cache[key]
            self.tail = self.cache[key]
            return

        if key in self.cache:
            key_node = self.cache[key]
            key_node.val = value
            self.move_node_front(key_node)
            return

        else:
            if self.capacity == 1:
                del self.cache[self.head.key]
                self.cache[key] = Node(key, value)
                self.head = self.cache[key]
                self.tail = self.cache[key]
                return

            if len(self.cache) == self.capacity:
                tail_node = self.tail
                self.tail.prev.next = None
                self.tail = tail_node.prev
                key_to_evict = tail_node.key
                del self.cache[key_to_evict]
                del tail_node

            new_node = Node(key, value)
            self.cache[key] = new_node
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return