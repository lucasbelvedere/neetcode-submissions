'''
Input: capacity for the cache, then calls to get(key) and put(key, value)
Output: get returns the value of the key or -1 if it doesn't exist, put returns nothing

Approach: A hashmap + a doubly linked list, no dummy nodes.
- The hashmap is data[key] = node, so we can find any node in O(1).
- The linked list keeps the order of use. self.head is the most recently used and self.tail is the least recently used. Both are real nodes, or None when the cache is empty.
- Why doubly linked? Because to remove a node from the middle in O(1), we need its prev AND its next. With a singly linked list we would have to walk the list to find the prev, which is O(n).
- Why does Node keep the key? Because when we evict the tail, we need its key to also delete it from the hashmap.
- Since there are no dummies, remove and add need None checks:
    - remove: if the node has no prev, it was the head, so the head moves to node.next. If it has no next, it was the tail, so the tail moves to node.prev.
    - add: if there is a head, link it back to the new node. If there is no tail, the list was empty, so the new node is also the tail.
- Every time we get or put a key, that node becomes the most recently used, so we remove it from where it is and add it to the head.
- In put, if the key already exists, we remove the old node first so it doesn't count twice. Then we add the new node, and if we went over capacity, we evict the tail.
- Time: O(1) for both get and put, since hashmap lookups and linked list add/remove are O(1).
- Space: O(capacity), since we store at most capacity nodes in the hashmap and the list.

PLAN:
- __init__:
    - self.capacity = capacity
    - self.data = {} (hashmap of key -> node)
    - self.head, self.tail = None, None
- remove(node):
    - if node.prev: node.prev.next = node.next, else self.head = node.next
    - if node.next: node.next.prev = node.prev, else self.tail = node.prev
    - node.prev, node.next = None, None
- add(node): (always to the head)
    - node.next = self.head
    - if self.head: self.head.prev = node
    - self.head = node
    - if not self.tail: self.tail = node
- get(key):
    - if key not in self.data: return -1
    - node = self.data[key]
    - remove(node), add(node) since it was just used
    - return node.val
- put(key, value):
    - if key in self.data: remove(self.data[key])
    - node = Node(key, value), self.data[key] = node, add(node)
    - if len(self.data) > self.capacity:
        - lru = self.tail
        - remove(lru), del self.data[lru.key]
'''

class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.head = None # Most recently used
        self.tail = None # Least recently used

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev, node.next = None, None

    def add(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        node = self.data[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.remove(self.data[key])
        node = Node(key, value)
        self.data[key] = node
        self.add(node)

        if len(self.data) > self.capacity:
            lru = self.tail
            self.remove(lru)
            del self.data[lru.key]