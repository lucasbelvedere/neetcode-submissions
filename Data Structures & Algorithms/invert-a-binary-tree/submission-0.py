# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque()
        queue.append(root)
        
        while len(queue) > 0:
            mainNode = queue[0]
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    tmp = node.left
                    node.left = node.right
                    node.right = tmp
            if mainNode.right:
                queue.append(mainNode.right)
            if mainNode.left:
                queue.append(mainNode.left)
        return root