# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        else:
            parent = None
            tmp = root
            while tmp and tmp.val != key:
                parent = tmp
                if tmp.val > key:
                    tmp = tmp.left
                else:
                    tmp = tmp.right
            if not tmp:
                return root
            # one child or no child
            if not tmp.left or not tmp.right:
                child = tmp.left if tmp.left else tmp.right
                if not parent: # a tree where key = root.key and root only has one child, all you do is return the child
                    return child
                if parent.left == tmp:
                    parent.left = child
                else:
                    parent.right = child
            else: # two children
                par = None
                delNode = tmp
                tmp = tmp.right
                while tmp.left:
                    par = tmp
                    tmp = tmp.left

                if par: # readjust the leaf to be moved into delete node, as well as it's parent
                    par.left = tmp.right
                    tmp.right = delNode.right
                tmp.left = delNode.left

                if not parent: # if node to be deleted is the root, just return tmp
                    return tmp

                if parent.left == delNode:
                    parent.left = tmp
                else:
                    parent.right = tmp
            return root
            