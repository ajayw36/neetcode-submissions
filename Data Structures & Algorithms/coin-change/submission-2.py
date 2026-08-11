class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount + 1] * (amount + 1)
        memo[0] = 0
        for i in range(1, amount+1):
            memo[i] = min((memo[i-coin] for coin in coins if i - coin >= 0), default = amount) + 1
        
        return memo[amount] if memo[amount] <= amount else -1
