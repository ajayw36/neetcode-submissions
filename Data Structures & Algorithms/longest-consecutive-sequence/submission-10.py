class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        starts = []
        for num in nums:
            if num-1 not in nums:
                starts.append(num)

        res = 0
        for start in starts:
            curr = start
            count = 1
            while curr + 1 in nums:
                curr = curr + 1
                count += 1
            res = max(count, res)
        
        return res