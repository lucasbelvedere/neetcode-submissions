# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Input: the root of a binary tree
Output: total number of nodes where their child's value sum to be equal to the node's value

Approach: Based on the constraints, we can't use recursion, but we can definitely traverse this binary tree with a post order using a stack, which is also a DFS approach.

PLAN:
- if not root, return 0
- new _stack and _sum equals to empty stack
- while _stack:
    - if node dot left exists:
        - add to the stack
    - if node dot right exists
        - add to the stack
- Declare a total dict
- Declare a res equals 0
- for node in _stack but reversed:
    - descendents equals to total dot get descendant left plus total dot get descendant right
    - res plus equals to node dot value == descendents
    - total sub node equals to node dot val
'''

class Solution:
    def equalToDescendants(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        _stack = [root]
        
        for node in _stack:
            if node.left:
                _stack.append(node.left)
            if node.right:
                _stack.append(node.right)

        total = {}
        res = 0

        for node in reversed(_stack):
            descendants = total.get(node.left, 0) + total.get(node.right, 0)
            res += node.val == descendants
            total[node] = descendants + node.val

        return res

            