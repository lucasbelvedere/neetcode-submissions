# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, node = None, None

        while list1 or list2:
            newNode = None
            if list1 and list2:
                if list1.val <= list2.val:
                    newNode = ListNode(list1.val, None)
                    list1 = list1.next
                else:
                    newNode = ListNode(list2.val, None)
                    list2 = list2.next
            elif list1:
                newNode = ListNode(list1.val, None)
                list1 = list1.next
            else:
                newNode = ListNode(list2.val, None)
                list2 = list2.next
            if not head:
                head = newNode
            else:
                node.next = newNode
            node = newNode
        return head

        