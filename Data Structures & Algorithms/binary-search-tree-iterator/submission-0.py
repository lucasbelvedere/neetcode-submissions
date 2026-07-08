# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.node = root

    def next(self) -> int:
        while self.node: # O(h) worst case
            self.stack.append(self.node)
            self.node = self.node.left
        node = self.stack.pop()
        self.node = node.right
        return node.val

    def hasNext(self) -> bool:
        return bool(self.node) or bool(self.stack)
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()