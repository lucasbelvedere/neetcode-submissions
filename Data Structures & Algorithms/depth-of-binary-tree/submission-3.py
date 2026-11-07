# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Input: Root of a BT
Output: The depth (integer) of a tree

Approach: to use recursion and, on each call stack, pass a level + 1.
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxLevel = [0]

        def dfs(root, level):
            if not root:
                return

            if level > maxLevel[0]:
                maxLevel[0] = level

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 1)
        return maxLevel[0]