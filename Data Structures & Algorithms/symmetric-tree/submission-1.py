# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Input: the root of a tree
Output: True if the tree is symmetric, False otherwise

Approach: recursively compare the left node's value with the right node's value, checking that the outer and inner children mirror each other

PLAN:
- def a helper function that takes two nodes
- if not left and not right:
    - return True
- elif not left or not right:
    - return False
- return left.val == right.val and a recursive call on (left.left, right.right) and a recursive call on (left.right, right.left)
- return a call to the helper function with root.left, root.right
'''

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def pre_order(left: TreeNode, right: TreeNode):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return left.val == right.val and pre_order(left.left, right.right) and pre_order(left.right, right.left)

        return pre_order(root.left, root.right)

# Time complexity: O(n), where n is the total # of nodes, since we visit each node once
# Space complexity: O(h), where h is the height of the tree, since the recursion stack goes at most h calls deep (O(log(n)) if balanced, O(n) if skewed)