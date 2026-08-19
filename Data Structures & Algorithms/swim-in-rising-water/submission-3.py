# Modified Djikstras
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)] # (height, r, c)
        visit = set()

        while heap:
            height, r, c = heapq.heappop(heap)
            if (r, c) == (n-1, n-1):
                return height
            
            for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                if 0 <= r + dr < n and 0 <= c + dc < n and (r + dr, c + dc) not in visit:
                    visit.add((r + dr, c + dc))
                    heapq.heappush(heap, (max(height, grid[r + dr][c + dc]), r + dr, c + dc))
        




