class Node:
    def __init__(self, key=0, value=0):
        self.key = key      # <-- needed so eviction can del from the map
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}          # key -> Node
        # dummy head/tail sentinels so every real node has two real neighbors
        self.left = Node()       # LRU side
        self.right = Node()      # MRU side
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert(self, node):
        # insert right before self.right (MRU end)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert(node)   # mark as most recently used
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next          # node just after left sentinel
            self._remove(lru)
            del self.cache[lru.key]       # <-- this is why the node needs .key