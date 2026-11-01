class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    res += 1
                    stack = [(i, j)]
                    while stack:
                        r, c = stack.pop()
                        for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
                            if 0 <= r + dr < n and 0 <= c + dc < m and  grid[r + dr][c + dc] == '1':
                               grid[r + dr][c + dc] = '0'
                               stack.append((r + dr, c + dc))
        return res 

