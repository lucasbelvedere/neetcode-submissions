"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
Input: a node from the graph
Output: a deep copy of this graph

Approach: BFS of the graph. For every node we visit for the first time, we create a copy of it with the same value and an empty neighbors list. Since the graph is undirected, each edge already appears in both nodes' neighbor lists, so when a node pops from the queue, we only add its neighbors' copies to its own copy. The other direction gets added when that neighbor pops.

PLAN:
- if not node:
    - return None

- firstNode = Node(node.val, [])
- visited, queue = {node: firstNode}, deque([node])

* temp refers to the original nodes in the graph
* visited also tracks the original nodes, but it maps each one to its copy, which builds the connection between the original graph and the new copy

- while queue:
    - temp = queue.popleft()
    - for neighbor in temp.neighbors:
        - if neighbor not in visited:
            - visited[neighbor] = Node(neighbor.val, [])
            - queue.append(neighbor)
        - visited[temp].neighbors.append(visited[neighbor])

- return firstNode
'''

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        firstNode = Node(node.val, [])
        visited, queue = {node: firstNode}, deque([node])

        while queue:
            temp = queue.popleft()
            for neighbor in temp.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[temp].neighbors.append(visited[neighbor])

        return firstNode
        