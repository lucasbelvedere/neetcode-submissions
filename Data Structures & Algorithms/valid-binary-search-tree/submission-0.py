# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        tmp = root
        prevVal = float("-inf")

        while tmp or stack:
            while tmp:
                stack.append(tmp)
                tmp = tmp.left
            tmp = stack.pop()
            if tmp.val <= prevVal:
                return False
            prevVal = tmp.val
            tmp = tmp.right
        return True