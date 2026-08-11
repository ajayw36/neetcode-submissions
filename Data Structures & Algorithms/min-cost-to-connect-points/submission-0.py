import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        costs = [[0] * len(points) for point in points]
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    costs[i][j] = float('inf')
                else:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    cost =  abs(x1 - x2) + abs(y1 - y2)
                    costs[i][j] = cost
                
        res = 0
        visited = set()
        min_heap = [] # list of [cost, point #]
        min_heap.append([0, 0])

        while len(visited) < len(points):
            cost, i = heapq.heappop(min_heap)
            if i not in visited:
                visited.add(i)
                res += cost
                for nei, nei_cost in enumerate(costs[i]):
                    heapq.heappush(min_heap, [nei_cost, nei])
                
        return res
