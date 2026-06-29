class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        
        self.next = self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def delete(self, node):
        previos, nxt = node.prev, node.next
        previos.next, nxt.prev = nxt, previos
    
    def insert(self, node):
        nxt = self.right
        previous = self.right.prev

        previous.next = node
        node.prev = previous
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]
