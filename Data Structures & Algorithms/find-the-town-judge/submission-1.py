class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees = [0] * n
        outdegrees = [0] * n

        for a, b in trust:
            indegrees[b-1] += 1
            outdegrees[a-1] += 1
        
        for i in range(n):
            if indegrees[i] == n - 1 and outdegrees[i] == 0:
                return i + 1
        
        return -1



        
