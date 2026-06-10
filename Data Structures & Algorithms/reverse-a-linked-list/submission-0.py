# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        tmp = head

        while tmp != None: # traverse through all nodes
            stack.append(tmp.val)
            tmp = tmp.next
        
        prevNode = None
        newHead = None
        while stack:          
            node = ListNode(stack.pop())
            if prevNode != None:
                prevNode.next = node
            if newHead == None:
                newHead = node
            prevNode = node
        return newHead



