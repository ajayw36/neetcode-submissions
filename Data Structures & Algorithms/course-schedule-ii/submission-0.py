class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {i : [] for i in range(numCourses)}
        for crs, prq in prerequisites:
            prereqs[crs].append(prq)
        
        cycle, visit = set(), set()
        res = []

        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            
            cycle.add(c)
            for prq in prereqs[c]:
                if dfs(prq) == False:
                    return False
            cycle.remove(c)

            visit.add(c)
            res.append(c)
        
        for c in prereqs.keys():
            if dfs(c) == False:
                return []
        
        return res