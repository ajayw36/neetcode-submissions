# Need to detect cycles within the graph. Can use a DFS strategy on every node to detect a cycle which repeats that node

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        path = set()
        def detect_cycle(course):
            if course in path: return True
            if graph[course] == []: return False

            path.add(course)
            for nei in graph[course]:
                if detect_cycle(nei): return True
            path.remove(course)
            graph[course] = []
            return False
        
        for course in range(numCourses):
            if detect_cycle(course): return False
        
        return True

