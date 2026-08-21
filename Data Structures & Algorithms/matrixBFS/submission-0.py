class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        q = collections.deque([(0, 0)])
        visit = set()
        res = 0
        n, m = len(grid), len(grid[0])
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if i == n - 1 and j == m - 1:
                    return res
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= i + di < n and 0 <= j + dj < m and (i + di, j + dj) not in visit and grid[i + di][j + dj] == 0:
                        visit.add((i + di, j + dj))
                        q.append((i + di, j + dj))
            res += 1
        
        return -1

        
        