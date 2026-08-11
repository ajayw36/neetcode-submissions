class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(2, len(nums) + 1):
            if i - 2 >= 0:
                memo[i] = max(memo[i-2], memo[i])
            if i - 3 >= 0:
                memo[i] = max(memo[i-3], memo[i])
            memo[i] += nums[i-1]
        return max(memo[len(nums)], memo[len(nums) - 1])