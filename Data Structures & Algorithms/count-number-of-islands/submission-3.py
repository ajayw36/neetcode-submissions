class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        stack = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    stack.append((i, j))
                    while stack:
                        cell = stack.pop()
                        r, c = cell[0], cell[1]
                        if r - 1 >= 0 and grid[r-1][c] == "1":
                            grid[r-1][c] = "0"
                            stack.append((r-1, c))
                        if r + 1 < len(grid) and grid[r+1][c] == "1":
                            grid[r+1][c] = "0"
                            stack.append((r+1, c))
                        if c - 1 >= 0 and grid[r][c-1] == "1":
                            grid[r][c-1] = "0"
                            stack.append((r, c-1))
                        if c + 1 < len(grid[0]) and grid[r][c+1] == "1":
                            grid[r][c+1] = "0"
                            stack.append((r, c+1))
        return res
