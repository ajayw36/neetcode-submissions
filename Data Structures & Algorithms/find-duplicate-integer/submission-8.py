class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if num < 0: num = -1 * num
            if nums[num - 1] < 0:
                return num
            nums[num - 1] = -1 * nums[num - 1]
    