# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        tmp = root
        goodNodes = 0
        curMax = float('-inf')          # max among tmp's ancestors

        # preorder iterative dfs
        while tmp or stack:
            while tmp:
                if curMax <= tmp.val:
                    goodNodes += 1
                curMax = max(curMax, tmp.val)
                stack.append([tmp, curMax])     # [1] = max including this node
                tmp = tmp.left
            tmp, curMax = stack.pop()   # restore max before going right
            tmp = tmp.right
        return goodNodes
            
