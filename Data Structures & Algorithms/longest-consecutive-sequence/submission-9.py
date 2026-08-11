class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        starts = []
        for num in nums:
            if num-1 not in nums:
                starts.append(num)

        res = 0
        for start in starts:
            count = 1
            while start + 1 in nums:
                count += 1
                start = start + 1
            res = max(count, res)

        return res
