class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = {}
        for num in nums:
            if num - 1 in nums:
                continue
            starts[num] = []
        
        
        for start in starts:
            current = start
            while current in nums:
                starts[start].append(current)
                current += 1
        
        res = 0

        for start in starts:
            if len(starts[start]) > res:
                res = len(starts[start])

        return res