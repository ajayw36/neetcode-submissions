# Top Down DP

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, bought):
            if i >= len(prices): return 0

            state = (i, bought)
            if state in dp:
                return dp[state]
            if bought:
                sell = prices[i] + dfs(i + 2, False)
                hold = dfs(i + 1, True)
                dp[state] = max(sell, hold)
            else:
                # buy
                buy = -prices[i] + dfs(i + 1, True)
                wait = dfs(i + 1, False)
                dp[state] = max(buy, wait)
            return dp[state]
        
        return dfs(0, False)
