'''
Input: an integer numCourses that represents how many courses you have to take, and an array prerequisites, where each list inside it shows that the course at index 1 is a prerequisite for the course at index 0
Output: True if it is possible to take all the courses, False otherwise

Approach: use Kahn's algorithm for topological sort, where we can only insert a graph node into the BFS queue once everything it depends on is done. The tricky part of this question is that we don't start with a graph, so we need to build one from prerequisites.
We need to be careful when doing that: each list in prerequisites means the node at index 1 points to the node at index 0, and not the opposite.
If there's a cycle, the courses in it never reach an indegree of 0, so they never enter the queue, and the count ends up smaller than numCourses.

Plan:
- declare and initialize a defaultdict(list) called graph
- for every list inside of prerequisites:
    - knowing each one has len == 2, we add the node at index 0 to the list of the node at index 1 in graph
- declare and initialize another dict called indegree, with every course from 0 to numCourses - 1 starting at 0
- loop through graph, adding to indegree the count of nodes that point to each node
- declare and initialize a queue with every node whose indegree equals 0
- declare and initialize count = 0
- while queue:
    - count += 1
    - temp = queue.popleft()
    - for i in graph[temp]:
        - indegree[i] -= 1
        - if indegree[i] == 0:
            - add i to the queue
- return count == numCourses

Time complexity: O(V + E), where V is numCourses and E is len(prerequisites), since we visit each course once and each edge once
Space complexity: O(V + E) for the graph, the indegree dict, and the queue
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        graph = defaultdict(list)
        for edges in prerequisites:
            graph[edges[1]].append(edges[0])

        indegree = {i: 0 for i in range(numCourses)}

        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] = indegree.get(neighbor, 0) + 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0]) # need to traverse graph, not indegree!
        count = 0

        while queue:
            count += 1
            temp = queue.popleft()
            for neighbor in graph[temp]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses
