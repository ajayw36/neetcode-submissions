class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, res = 0, 0, 0
        while j < len(prices):
            if prices[i] < prices[j]:
                res = max(res, prices[j] - prices[i])                
            else:
                i = j
            j += 1
        return res
        
            
        