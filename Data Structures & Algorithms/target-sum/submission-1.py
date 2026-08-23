# Top Down DP
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {} # key is (i, curr)
        def dfs(i, curr): 
            '''
            Returns the number of paths to get to the target starting with index i and current sum curr. Eventually we want dfs(0, 0)
            '''
            if (i, curr) in dp:
                return dp[(i, curr)]
            if i == n:
                if curr == target:
                    dp[(i, curr)] = 1
                    return 1
                dp[(i, curr)] = 0
                return 0
            
            res = dfs(i + 1, curr + nums[i]) + dfs(i + 1, curr - nums[i])
            dp[(i, curr)] = res
            return res
        

        return dfs(0, 0)