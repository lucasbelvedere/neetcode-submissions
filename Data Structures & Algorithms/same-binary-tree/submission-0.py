# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        leftList, rightList = [], []

        def bfs(root, nodeList):
            queue = deque()
            queue.append(root)
            while queue:
                node = queue.popleft()
                if not node:
                    nodeList.append(None)
                else:
                    nodeList.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
        
        bfs(p, leftList)
        bfs(q, rightList)
        return leftList == rightList
