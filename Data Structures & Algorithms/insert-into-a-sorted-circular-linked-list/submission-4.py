# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

'''
Input: the head of a linked list, as well as an insertVal that we need to insert into the circular linked list
Output: the head of this circular linked list

Approach: traverse the linked list, and insert the new value whenever we either find a value greater than or equal to insertVal, create a new node, and insert it right before this
node.

In case the list is empty, then just create a new node, make next point to itself, and return.

PLAN:
- If head is none, head equals to new node, new node.next = new node.
- prev, temp = None, head
- while true:
    - if prev.value > temp.value and prev.value <= insertValue:
        - insert value on prev.next, and then ensure the new node point to temp.
    - elif temp.value >= insertValue:
        - regular insert here
    - prev = temp
    - temp = temp.next
    - if temp == head:
        - in this case, we looped through the whole list, and didn't find a good spot, so we insert this value in here and break the loop
- return head
'''


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        prev, temp = head, head.next
        while True:
            if prev.val <= insertVal and temp.val > insertVal:
                prev.next = Node(insertVal, temp)
                break
            elif prev.val > temp.val and (temp.val >= insertVal or prev.val <= insertVal):
                prev.next = Node(insertVal, temp)
                break
            prev = temp
            temp = temp.next
            if prev == head:
                prev.next = Node(insertVal, temp)
                break

        return head

        