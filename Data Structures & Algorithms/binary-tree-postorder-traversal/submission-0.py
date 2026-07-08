# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [], []
        node, last_visited = root, None

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            peek = stack[-1]
            if peek.right and peek.right is not last_visited:
                node = peek.right          # right subtree not done yet
            else:
                res.append(peek.val)       # both subtrees done, visit
                last_visited = stack.pop()
        return res
            