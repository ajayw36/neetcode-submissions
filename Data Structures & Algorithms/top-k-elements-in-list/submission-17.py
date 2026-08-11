from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        elts = []
        for num, count in freq.items():
            heapq.heappush(elts, [-count, num])
        res = []
        for i in range(k):
            res.append(heapq.heappop(elts)[1])
        return res
