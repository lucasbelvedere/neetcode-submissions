# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Input: the root of a BT and an integer targetSum
Output: True if the tree has a root-to-leaf path that adds up to targetSum, False otherwise

Approach: recursively traverse the tree, subtracting each node's value from targetSum, and when reaching a leaf, check if the remaining target equals the leaf's value. Return True if it does, False otherwise

PLAN:
- if not root:
    - return False
- if not root.left and not root.right:
    - return targetSum - root.val == 0
- return a recursive call to the left with targetSum minus root.val OR a recursive call to the right with targetSum minus root.val
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

# Time complexity: O(n), where n is the number of nodes in the BT, since we visit each node at most once
# Space complexity: O(h), where h is the height of the tree, since the recursion stack goes at most h calls deep (O(log(n)) if balanced, O(n) if skewed)