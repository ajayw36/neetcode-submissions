class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)
        memo[0] = 0
        for i in range(1, amount + 1):
            coin_amounts = []
            for coin in coins:
                if i - coin >= 0 and memo[i-coin] != -1:
                    coin_amounts.append(memo[i-coin])
            if coin_amounts:
                min_coin_amount = min(coin_amounts)
                memo[i] = min_coin_amount + 1
        
        return memo[amount]