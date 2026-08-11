class Solution:
    def binary_search(self, left, right, nums, target):
        if left > right:
            return -1
        
        m = (left + right) // 2

        if nums[m] == target:
            return m 
        elif nums[m] < target:
            return self.binary_search(m+1, right, nums, target)
        else:
            return self.binary_search(left, m-1, nums, target)


    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        return self.binary_search(left, right, nums, target)

        


            
        
            
        