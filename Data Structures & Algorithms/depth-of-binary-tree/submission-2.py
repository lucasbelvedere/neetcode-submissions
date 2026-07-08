# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = []
        node = root
        depth, maxDepth = 1, 1

        while node or stack:
            while node:
                stack.append((node, depth))
                node = node.left
                depth += 1
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            if node.right:
                depth += 1
                node = node.right
            else:
                node = None
        return maxDepth
