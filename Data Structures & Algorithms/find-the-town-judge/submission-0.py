class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {i : set([i]) for i in range(1, n + 1)}
        for a, b in trust:
            graph[a].add(b)
        
        candidates = []
        for i in range(1, n + 1):
            if len(graph[i]) == 1:
                candidates.append(i)

        for i in candidates:
            found = True
            for j in graph:
                if i not in graph[j]:
                    found = False
                    break
            if found: return i

        return -1


        
