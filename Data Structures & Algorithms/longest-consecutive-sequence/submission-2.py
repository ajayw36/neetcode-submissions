class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = {}
        numset = set(nums)
        for num in numset:
            if num - 1 in numset:
                continue
            starts[num] = []
        
        
        for start in starts:
            current = start
            while current in numset:
                starts[start].append(current)
                current += 1
        
        res = 0

        for start in starts:
            if len(starts[start]) > res:
                res = len(starts[start])

        return res