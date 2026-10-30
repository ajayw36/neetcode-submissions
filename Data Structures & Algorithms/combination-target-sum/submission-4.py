class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        sum = 0
        n = len(nums)
        res = []
        def search(i):
            nonlocal sum
            if sum == target:
                res.append(curr.copy())
                return
            if i == n:
                return
            
            if sum > target:
                return
            
            curr.append(nums[i])
            sum += nums[i]
            search(i)
                        
            curr.pop()
            sum -= nums[i]
            search(i + 1)
        
        search(0)
        return res