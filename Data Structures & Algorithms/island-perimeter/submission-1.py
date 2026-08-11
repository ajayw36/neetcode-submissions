class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        searched = [[False for  i in range(len(grid[0]))] for j in range(len(grid))]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            perimeter = 0
            stack = []
            stack.append([i, j])
            while stack:
                cell = stack.pop()
                r, c = cell[0], cell[1]
                if searched[r][c]:
                    continue
                searched[r][c] = True
                num_connections = 0
                if r + 1 < rows and grid[r + 1][c] == 1:
                    num_connections += 1
                    stack.append([r + 1, c])
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    num_connections += 1
                    stack.append([r - 1, c])
                if c + 1 < cols and grid[r][c + 1] == 1:
                    num_connections += 1
                    stack.append([r, c + 1])
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    num_connections += 1
                    stack.append([r, c - 1])
                perimeter += (4 - num_connections)
            return perimeter
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i,j)
