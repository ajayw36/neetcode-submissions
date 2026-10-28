class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        n = len(nums)
        curr = []
        def dfs(i):
            if i == n:
                res.append(curr.copy())
                return
            dfs(i + 1)
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()
    
        dfs(0)
        return res