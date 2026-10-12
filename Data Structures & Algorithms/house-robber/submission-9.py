# Bottom up recursion
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-float('inf')] * (n + 1)
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(2, n + 1):
            memo[i] = max(nums[i-1] + memo[i - 2], memo[i - 1])
        return memo[n]
