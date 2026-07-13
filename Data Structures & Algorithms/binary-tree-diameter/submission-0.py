# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            if not root: # base case
                return 0
            nonlocal res # allows you to modify a variable in an outer (enclosing) function's scope from within a nested inner function

            # recursive cases
            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, left + right)
            return max(left, right) + 1

        dfs(root)
        return res

