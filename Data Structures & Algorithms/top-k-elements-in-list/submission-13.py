class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)] #because I don't feel like subtracting one for zero indexing

        for num, frequency in frequencies.items():
            buckets[frequency].append(num)
        
        res = []
        
        while len(res) < k:
            bucket = buckets.pop()
            for num in bucket:
                res.append(num)
        
        return res
