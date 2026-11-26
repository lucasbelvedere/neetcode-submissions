'''
Input: an int n (the number of nodes, labeled 0 to n - 1) and an edges list (for an undirected graph)
Output: True if the graph is a valid tree, False otherwise

Approach: run BFS. A graph is a valid tree when it has no cycles and all the nodes are connected. While running BFS, if we find a neighbor that is already visited and it isn't the parent of the current node, then there's a cycle, so it's not a valid tree. At the end, if the BFS didn't reach every node, the graph isn't connected, so it's not a valid tree either.

Plan:
- Declare and initialize graph based on the edges list (add both directions, since it's undirected)
- Declare and initialize the queue with node 0 and its parent, (0, -1), and visited with node 0
- count = 0
- while queue:
    - count += 1
    - temp, parent = queue.popleft()
    - for neighbor in graph[temp]:
        - if neighbor == parent:
            - continue
        - if neighbor in visited:
            - return False
        - else:
            - add neighbor to visited, and (neighbor, temp) to the queue
- return count == n

Time and space complexity: O(V + E)
'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n <= 1
        
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        queue = deque([(0, -1)])
        visited = set([0])

        count = 0
        while queue:
            count += 1
            temp, parent = queue.popleft()
            for neighbor in graph[temp]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                queue.append((neighbor, temp))
        
        return count == n

        