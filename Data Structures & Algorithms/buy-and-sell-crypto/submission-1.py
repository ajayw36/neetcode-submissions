class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, profit = 0, 1, 0

        while r < len(prices):
            profit = max(prices[r] - prices[l], profit)
            if prices[l] > prices[r]:
                l += 1
                r = l
            r += 1

        return profit

            