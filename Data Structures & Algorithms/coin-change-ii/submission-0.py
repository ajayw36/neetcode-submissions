class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(1, amount + 1):

                # use coin
                coin = coins[i]
                use = dp[i][j - coin] if j - coin >= 0 else 0

                # don't use
                no_use = dp[i + 1][j] if i + 1 < n else 0

                dp[i][j] = use + no_use
        
        return dp[0][amount]