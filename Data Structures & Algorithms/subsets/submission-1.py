class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        n = len(nums)
        def dfs(i, curr):
            if i == n:
                res.append(curr)
                return
            dfs(i + 1, curr.copy())
            curr.append(nums[i])
            dfs(i + 1, curr.copy())
    
        dfs(0, [])
        return res