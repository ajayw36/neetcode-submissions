class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0: return 0

        res = 0
        n = len(grid)
        m = len(grid[0])
        visit = set([(0, 0)])


        def dfs(i, j):
            nonlocal res
            if (i, j) == (n - 1, m - 1):
                res += 1
                return
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if 0 <= i + di < n and 0 <= j + dj < m and (i + di, j + dj) not in visit and grid[i + di][j + dj] == 0:
                    visit.add((i + di, j + dj))
                    dfs(i + di, j + dj)
                    visit.remove((i + di, j + dj))
        
        dfs(0, 0)
        return res
            
            
            
