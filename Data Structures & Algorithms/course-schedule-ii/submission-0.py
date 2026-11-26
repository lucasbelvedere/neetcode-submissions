'''
Input: an array prerequisites, where each array inside it, [a, b], means you must take course b before taking course a, and numCourses, the number of courses you are required to take
Output: a valid order of courses you can take to finish all courses, or an empty array if it's impossible

Approach: Topological sort. We must first create a graph from prerequisites, and then, from this graph, create another dict that tells us how many prerequisites each node has. With this dict, we can then run BFS with topological sort and build the order. If the order doesn't contain every course, there's a cycle, so there's no solution.

Edge cases: if prerequisites is empty, every course can be taken in any order.

Plan:
- declare and initialize graph, and for every edge [a, b] in prerequisites, add a to b's list
- declare and initialize indegree for every course from 0 to numCourses - 1, which counts how many prerequisites each course has
- declare and initialize a queue with all the nodes whose indegree equals 0
- res = []
- while queue:
    - temp = queue.popleft()
    - res.append(temp)
    - for neighbor in graph[temp]:
        - indegree[neighbor] -= 1
        - if indegree[neighbor] == 0:
            - add it to the queue
- return [] if len(res) != numCourses else res

Time complexity: O(V + E), where V and E represent the total number of vertices and edges
Space complexity: O(V + E) from the graph
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        indegree = {i: 0 for i in range(numCourses)}

        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] = indegree.get(neighbor, 0) + 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        res = []
        while queue:
            temp = queue.popleft()
            res.append(temp)
            for neighbor in graph[temp]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return [] if len(res) != numCourses else res



        