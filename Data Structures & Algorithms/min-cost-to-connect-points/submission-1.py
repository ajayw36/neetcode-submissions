class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        visited = [False] * n
        distances = [float('inf')] * n
        edges, res = 0, 0

        def getManhattanDistance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)

        while edges < n - 1:
            visited[node] = True
            next_node = -1
            min_dist = float('inf')
            for i, point in enumerate(points):
                if visited[i] == True:
                    continue
                distances[i] = min(distances[i], getManhattanDistance(points[node], point))
                if distances[i] < min_dist:
                    min_dist = distances[i]
                    next_node = i
            if next_node != -1:
                res += min_dist
                edges += 1
                visited[next_node] = True
                node = next_node
        
        return res

