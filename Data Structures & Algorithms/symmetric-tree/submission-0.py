# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Input: the root of a tree
Output: True if the tree is symmetric, false otherwise

Approach: recursively compare if node left's value equals to node right's value

PLAN:
- def a helper function that takes two nodes
- if not left and not right
    - return True
- elif not left or not right:
    - return False
- return left == right and recursive call of (left.right, right.left) and recursive call (left.left, right.right)
- return call to helper function with root.left, root.right
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

# Time complexity: O(n), where n is total # of nodes
# Space complexity: O(log(n)), since we will recursively have at most log(n) recursive calls in the stack