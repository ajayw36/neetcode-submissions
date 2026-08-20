class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)] #[bought = False, bought = True]

        for i in range(n - 1, -1, -1):
            price = prices[i]

            # Haven't bought yet, either buy or wait
            buy = -price + dp[i + 1][1] if i + 1 < n else 0
            wait = dp[i + 1][0] if i + 1 < n else 0

            dp[i][0] = max(buy, wait)

            # Bought, either sell or hold
            sell = price + dp[i + 2][0] if i + 2 < n else price
            hold = dp[i + 1][1] if i + 1 < n else 0

            dp[i][1] = max(sell, hold)
        
        return dp[0][0]
