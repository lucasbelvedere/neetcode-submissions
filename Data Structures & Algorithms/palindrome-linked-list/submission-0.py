# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Input: the head of a list
Output: a boolean that represents rather if the list is a palinfrome or not

Approach: by using the slow/fast two pointers approach, we find the middle of the linked list. Then, on the second half, we reverse it. Later on, we compare both halfs in O(n) and O(1) space.

This is changing the original list, but since this is a leetcode problem, we are assuming this is no big deal.

PLAN:
- slow, fast = head
- while fast and fast.next:
    - slow = slow.next
    - fast = fast.next.next
- fast = slow
- temp = slow.next
- slow.next = None
- while temp:
    - temp2 = temp.next
    - temp.next = slow
    - slow = temp
    - temp = temp2
- temp = head
- while temp != fast:
    - if temp.val != slow.val:
        - return False
    - temp = temp.next
    - slow = slow.next
- return True
'''

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        fast = slow
        temp = slow.next
        slow.next = None # Not important, just to visually see the second half be limited by a None
        
        while temp:
            temp2 = temp.next
            temp.next = slow
            slow = temp
            temp = temp2

        temp = head
        
        while temp != fast:
            if temp.val != slow.val:
                return False
            temp = temp.next
            slow = slow.next

        return True
