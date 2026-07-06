# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack, counter = [], 0
        tmp = root
        while tmp or stack:
            while tmp:
                stack.append(tmp)
                tmp = tmp.left
            tmp = stack.pop()
            counter += 1
            if counter == k:
                return tmp.val
            tmp = tmp.right
        return res[k - 1]