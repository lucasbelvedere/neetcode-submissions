# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Input: root of a BST
Output: root of the BST but with all the left and right child inverted

Approach: Use recursion to traverse through the BST, if left, then call it recursively to the right, else call if recursively to the left, and return root
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root