# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack, res = [], []
        tmp = root
        while tmp or stack:
            while tmp:
                stack.append(tmp)
                tmp = tmp.left
            tmp = stack.pop()
            res.append(tmp.val)
            if len(res) == k:
                return res[-1]
            tmp = tmp.right
        return res[k - 1]