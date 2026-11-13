# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Input: the head of a linked list and a positive integer k
Output: the head of the list with every group of k nodes reversed (leftover nodes at the end stay in their original order)

Approach: 1st, we count how many nodes there are in the linked list so we can divide that by k. That way, we know we will have to reverse n//k groups.
2nd, we declare a function invert_k_nodes that reverses k nodes in the list. It takes the head of the group, the tail of the previous group, and k, and it returns the new head of the group and the first node of the next group.
3rd, in a loop, we call invert_k_nodes n//k times.

PLAN:
- declare count_nodes that takes a head and returns the number of nodes in the list
- declare invert_k_nodes that takes head, prev_tail, and k
    - prev = None
    - temp = head
    - for i in range of k:
        - nxt = temp.next
        - temp.next = prev
        - prev = temp
        - temp = nxt
    - head.next = temp (the old head is now the tail, so connect it to the rest of the list)
    - if prev_tail:
        - prev_tail.next = prev (connect the previous group to the new head of this group)
    - return prev, temp
- in reverse_k_group:
    - kgroups = count_nodes(head) // k
    - start = head, prev_tail = None
    - for i in range of kgroups:
        - new_head, next_start = invert_k_nodes(start, prev_tail, k)
        - if i == 0:
            - head = new_head
        - prev_tail = start
        - start = next_start
    - return head
'''

class Solution:
    def countNodes(self, temp: Optional[ListNode]) -> int:
        count = 0

        while temp:
            temp = temp.next
            count += 1

        return count

    def invertKnodes(self, head: Optional[ListNode], prev_tail: Optional[ListNode], k):
        prev = None
        temp = head
        
        for i in range(k):
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt

        head.next = temp
        if prev_tail:
            prev_tail.next = prev

        return prev, temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kgroups = self.countNodes(head) // k

        start = head
        prev_tail = None

        for i in range(kgroups):
            new_head, next_start = self.invertKnodes(start, prev_tail, k)
            if i == 0:
                head = new_head
            prev_tail = start
            start = next_start

        return head
            
        