class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        res = 0
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j = i + 1
            if j < len(prices):
                res = max(res, prices[j] - prices[i])
            j += 1
        return res