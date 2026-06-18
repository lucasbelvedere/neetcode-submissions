# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp, val = head, 0
        while tmp != None:
            val += 1
            tmp = tmp.next
        node = val - n # this will give the node to be removed
        tmp, prev = head, None
        while tmp != None:
            if node == 0:
                if prev == None:
                    head = head.next
                else:
                    prev.next = tmp.next
                break
            prev = tmp
            tmp = tmp.next
            node -= 1
        return head
    
        