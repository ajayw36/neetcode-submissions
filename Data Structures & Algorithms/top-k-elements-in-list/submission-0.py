class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        arr = []
        for num, count in counts.items():
            arr.append([count, num])
        arr.sort()

        res = []

        while k > 0:
            res.append(arr.pop()[1])
            k-=1
        
        return res