class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if n == 0:
            return 0

        min_times = [float('inf')] * (n+1)
        min_times[k] = 0
        min_times[0] = 0
        graph = defaultdict(list)
        min_heap = []
        visit = set([k, 0])

        for ui, vi, ti in times:
            graph[ui].append([vi, ti])

        for vi, ti in graph[k]:
            heapq.heappush(min_heap, [ti, vi])
        
        while min_heap and len(visit) < (n + 1):
            ti, ui = heapq.heappop(min_heap)
            if ui in visit:
                continue
            min_times[ui] = min(min_times[ui], ti)
            visit.add(ui)
            for vi, ti in graph[ui]:
                heapq.heappush(min_heap, [min_times[ui] + ti, vi])
        if len(visit) < (n+1):
            return -1
        return max(min_times)

