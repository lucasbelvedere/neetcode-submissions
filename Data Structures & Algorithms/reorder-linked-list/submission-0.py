# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        table, tmp, n = {}, head, 0
        while tmp:
            table[n] = tmp
            n += 1
            tmp = tmp.next
        for key, val in table.items():
            if key == (n // 2):
                val.next = None
            elif key > (n // 2):
                val.next = table[n - key]
            else:                
                val.next = table[n - key - 1]
