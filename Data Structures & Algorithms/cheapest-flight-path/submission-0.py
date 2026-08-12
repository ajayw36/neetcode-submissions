class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')] * n
        costs[src] = 0
        for _ in range(k+1):
            temp = [c for c in costs]
            for u, v, cost in flights:
                temp[v] = min(temp[v], costs[u] + cost)
            costs = temp
        return -1 if costs[dst] == float('inf') else costs[dst]
