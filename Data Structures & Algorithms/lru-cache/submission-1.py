class ListNode:

    def __init__(self, key,value):
        self.next = None
        self.prev = None
        self.value = value
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}
        
    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next,node.prev = nxt, prev


    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next,nxt.prev = nxt, prev    

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        
        return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        




        
