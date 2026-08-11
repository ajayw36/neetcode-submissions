class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods = [1 for num in nums]
        right_prods = [1 for num in nums]

        for i in range(1, len(nums)):
            left_prods[i] = left_prods[i-1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right_prods[i] = right_prods[i+1] * nums[i + 1]
        
        res = [left_prods[i] * right_prods[i] for i in range(len(nums))]
        return res