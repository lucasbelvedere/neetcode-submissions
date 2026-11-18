# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Input: the root of a binary tree
Output: True if the tree is height balanced, False otherwise

Approach: BFS to get every node in level order, then go through them in reverse to calculate heights from the bottom up.
- BFS goes top to bottom, but a node's height depends on its children. Reversing the BFS order guarantees children are processed before their parents.
- We keep a hashmap height[node] = height of that node. A missing child (None) has height 0, so we use height.get(child, 0).
- For every node, if the left and right heights differ by more than 1, return False right away.
- Time: O(n), where n is the total number of nodes, since each node is added to the queue once and processed once.
- Space: O(n) for the queue, the order list, and the height hashmap.

PLAN:
- if not root: return True
- q = deque([root]), order = []
- while q:
    - node = q.popleft()
    - order.append(node)
    - if node.left: q.append(node.left)
    - if node.right: q.append(node.right)
- height = {}
- for node in reversed(order):
    - left_height = height.get(node.left, 0)
    - right_height = height.get(node.right, 0)
    - if abs(left_height - right_height) > 1: return False
    - height[node] = 1 + max(left_height, right_height)
- return True
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root])
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        height = {}
        for node in reversed(order):
            left_height = height.get(node.left, 0)
            right_height = height.get(node.right, 0)

            if abs(left_height - right_height) > 1:
                return False

            height[node] = 1 + max(left_height, right_height)

        return True