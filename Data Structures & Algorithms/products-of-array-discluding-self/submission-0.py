import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            arr = nums[:i] + nums[i+1:]
            prod = math.prod(arr)
            res.append(prod)

        return res