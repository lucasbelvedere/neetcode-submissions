# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            tmp = root
            while True:                    
                if tmp.val > val:
                    if tmp.left:
                        tmp = tmp.left
                    else:
                        tmp.left = TreeNode(val)
                        return root
                else:
                    if tmp.right:
                        tmp = tmp.right
                    else:
                        tmp.right = TreeNode(val)
                        return root
        else:
            root = TreeNode(val)
        return root