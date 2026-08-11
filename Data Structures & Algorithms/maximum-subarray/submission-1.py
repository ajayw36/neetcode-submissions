class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = 0
        res = -float('inf')
        curr = 0
        while r < len(nums):
            curr += nums[r]
            res = max(res, curr)
            if curr < 0:
                curr = 0
            r += 1
        return res