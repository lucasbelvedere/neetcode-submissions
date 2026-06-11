# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, node, carry = None, None, 0

        while l1 or l2 or carry:
            val = carry
            val += l1.val if l1 else 0
            val += l2.val if l2 else 0
            carry, val = divmod(val, 10)
            newNode = ListNode(val, None)
            if not head:
                head = newNode
            if node:
                node.next = newNode
            node = newNode
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head

