class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        min_heap = []
        for num, frequency in frequencies.items():
            heapq.heappush(min_heap, [frequency, num])
            if len(min_heap) > k:    
                heapq.heappop(min_heap)
        
        res = []
        for elt in min_heap:
            res.append(elt[1])
        return res