# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Input: a list of head nodes (for linked lists)
Output: the head of a sorted linked list with all the lists merged

Approach: A min heap with the priority being the value of the node. This heap will heapify in O(k), where k is the total number of linked lists we have to merge.
- We add only the head of each list to the heap, as [value, counter, node]. The value goes first since it's the priority.
- The counter is a tiebreaker. If two nodes have the same value, Python compares the next element in the list, and comparing two ListNodes throws a TypeError. Since the counter is always unique, the comparison stops there and never reaches the nodes.
- But why not add ALL nodes from ALL the lists and heapify them? Because heapify would cost O(n), where n is the total number of nodes from all the lists, while heapifying only the heads costs O(k). That keeps our heap small and more efficient.
- Adding/removing from the heap costs O(log(k)), since the heap does NOT keep ALL the nodes in it. We just pop the node at the top and push that node's next one. Every node gets pushed and popped once, so the total is O(n*log(k)), where n is the total number of nodes and k is the total number of lists.
- Space: O(k), since the heap holds at most one node per list at a time.

PLAN:
- res, temp, minHeap, counter = None, None, [], 0
- for list_head in lists:
    - if list_head:
        - minHeap.append([list_head.val, counter, list_head]) so every item inside of minHeap is [priority/value, tiebreaker, node address]
        - counter += 1
- heapq.heapify(minHeap) so we turn the list into a min heap
- while minHeap:
    - node = heapq.heappop(minHeap)[2] so we grab the node itself, not the whole list
    - if not res:
        - res = node
        - temp = node
    - else:
        - temp.next = node
        - temp = temp.next
    - if node.next:
        - heapq.heappush(minHeap, [node.next.val, counter, node.next]) which is O(log(k))
        - counter += 1
- return res (no need for temp.next = None, since the last node popped already has no next, and it would crash if lists is empty)
'''

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res, temp, minHeap = None, None, []
        counter = 0

        for list_head in lists:
            if list_head:
                minHeap.append([list_head.val, counter, list_head])
                counter += 1

        heapq.heapify(minHeap)
        
        while minHeap:
            node = heapq.heappop(minHeap)[2]
            if not res:
                res = node
                temp = node
            else:
                temp.next = node
                temp = temp.next
            if node.next:
                heapq.heappush(minHeap, [node.next.val, counter, node.next])
                counter += 1
        
        return res

