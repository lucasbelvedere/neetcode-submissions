# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Given a root of a binary tree and an int target sum, we need to return True if the tree has a root-to-leaf path such that adding up all values along the path equals to targetSum

For that, we can run a DFS algorithm and backtrack whenever we know in that path there won't be a solution. Values can be negative, so we ONLY backtrack when we reach the leaf.

PLAN
- if not root, return False
- declare and initialize an empty stack for the sums
- declare and initialize another empty stack for the path and add root
- while path stack is not empty:
    - temp equals to path stack[-1]
    - temp sum equals to temp dot val
    - if sum stack
        - Add sum stack[-1] to temp sum
    - if not path.left and not path.right:
        - if temp sum equals to target value, then return True
        - else...
    - if path.right, then add to path.stack
    - if path.left, then add to path.stack
    - add temp sum to sum stack
- return False
'''
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = [(root, False)]
        sum = 0

        while stack:
            node, curr = stack.pop()

            if curr:
                sum -= node.val
                continue

            if not node:
                continue

            sum += node.val
            if not node.left and not node.right:
                if sum == targetSum:
                    return True
                sum -= node.val
                continue

            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
  
        return False
            
            
        