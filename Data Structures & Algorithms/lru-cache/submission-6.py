class Node:
    def __init__(self, key, value, prev = None, next = None):
        self.prev = prev
        self.next = next
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.front = Node(0, 0) # Least recent dummy
        self.back = Node(0, 0) # Most recent dummy
        self.front.next = self.back
        self.back.prev = self.front
        self.node_map = {} # Key --> Node
        self.size = 0
        self.capacity = capacity

    def insert(self, key, value):
        node = Node(key, value)
        prev = self.back.prev
        node.prev = prev
        prev.next = node

        node.next = self.back
        self.back.prev = node

        self.node_map[key] = node
        self.size += 1
    
    def remove(self, key):
        node = self.node_map[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        self.node_map.pop(key)
        self.size -= 1


    def get(self, key: int) -> int:
        if key in self.node_map:
            value = self.node_map[key].value
            self.remove(key)
            self.insert(key, value)
            return value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self.remove(key)
            self.insert(key, value)

        else:
            self.insert(key, value)

            if self.size > self.capacity:
                self.remove(self.front.next.key)
            

