# Define a class for a Node
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
     
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Map key to Node
        self.cache = {}
        # Dummy Nodes for Least Recent and Most Recent values
        self.left = Node(0, 0)
        self.right = Node (0, 0)
        # Connect these nodes to each other initially
        self.left.next = self.right
        self.right.prev = self.left
        # Every time we 

    # Remove from list
    def remove(self, node):
        # Make the pointer from previous node point to next node and 
        # pointer from next node point to previous node
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    # Insert node at right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        # If Node with same key already exists in cache, remove it
        if key in self.cache:
            self.remove(self.cache[key])
        # Make the pointer in the hashmap point to the new node
        self.cache[key] = Node(key, value)
        # Insert the node into the Doubly Linked List
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Remove from the LinkedList and delete LRU from hashmap
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
