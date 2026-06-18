"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr, tmp, head2, table = head, None, None, {}
        while ptr != None:
            node = Node(ptr.val, None, None)
            if head2 == None:
                head2 = tmp = node
            else:
                tmp.next = node
                tmp = tmp.next
            table[ptr] = tmp
            ptr = ptr.next
        ptr, tmp = head, head2
        while ptr != None:
            if ptr.random:
                tmp.random = table[ptr.random]
            ptr = ptr.next
            tmp = tmp.next
        return head2