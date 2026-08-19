class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heights = sorted([grid[i][j] for i in range(n) for j in range(n)])


        def dfs(src, height, visit):
            i, j = src
            if grid[i][j] > height: return False
            if (i, j) == (n - 1, n - 1): return True

            for di, dj in [0, 1], [0, -1], [1, 0], [-1, 0]:
                if 0 <= i + di < n and 0 <= j + dj < n and grid[i + di][j + dj] <= height and (i + di, j + dj) not in visit:
                    visit.add((i + di, j + dj))
                    if dfs((i + di, j + dj), height, visit):
                        return True

        l, r = 0, len(heights) - 1
        while l <= r:
            idx = (l + r) // 2
            height = heights[idx]
            visit = set()

            if dfs((0, 0), height, visit):
                r = idx - 1
            else:
                l = idx + 1


        return heights[l]