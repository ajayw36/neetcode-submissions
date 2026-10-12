# Bottom up space optimized
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2 = 0
        prev1 = nums[0]
        for i in range(2, n + 1):
            temp = prev1
            prev1 = max(nums[i-1] + prev2, prev1)
            prev2 = temp
        return prev1
