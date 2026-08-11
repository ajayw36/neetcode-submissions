from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        elts = []
        for num, count in freq.items():
            elts.append([count, num])
        elts.sort()
        res = []
        for i in range(k):
            res.append(elts[len(elts)-i-1][1])
        return res
