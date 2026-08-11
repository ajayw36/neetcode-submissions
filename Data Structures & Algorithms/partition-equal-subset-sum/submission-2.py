class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        m = sum(nums)

        if m % 2 == 1:
            return False

        dp = [[False] * (m // 2 + 1) for _ in range(n)]

        for i in range(n):
            for j in range(m // 2 + 1):
                curr = nums[i]
                if j == 0:
                    dp[i][j] = True
                    continue

                # exclude
                if i - 1 >= 0 and dp[i-1][j]:
                    dp[i][j] = True
                    continue
                
                # include
                if i - 1 >= 0 and j - curr >= 0 and dp[i-1][j-curr]:
                    dp[i][j] = True
        
        return dp[-1][-1]
