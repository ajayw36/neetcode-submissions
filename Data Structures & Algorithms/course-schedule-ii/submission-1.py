from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        q = deque()
        prqs = {i : [] for i in range(numCourses)}
        indeg = [0] * numCourses

        for crs, prq in prerequisites:
            prqs[prq].append(crs)
            indeg[crs] += 1
        for i, deg in enumerate(indeg):
            if deg == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            res.append(curr)
            for crs in prqs[curr]:
                indeg[crs] -= 1
                if indeg[crs] == 0:
                    q.append(crs)
        
        if len(res) != numCourses:
            return []
        return res
            

            
