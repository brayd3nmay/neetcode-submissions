class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity    
        self.cache = {} # key: Node
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def add(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        mru = self.right.prev
        mru.next, self.right.prev = new_node, new_node
        new_node.prev, new_node.next = mru, self.right
        self.cache[key] = new_node

    def remove(self, key: int) -> None:
        temp = self.cache[key]
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        del self.cache[key]

    def get(self, key: int) -> int:
        if key in self.cache:
            node_val = self.cache[key].value
            self.remove(key) 
            self.add(key, node_val)
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        self.add(key, value)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru.key)
