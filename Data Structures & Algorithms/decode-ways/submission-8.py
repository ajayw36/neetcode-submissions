class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] * (n+1)

        new_s = []
        for c in s:
            new_s.append(int(c))
        s = new_s

        for i in range(n-1, -1, -1):
            if s[i] == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if i < n - 1 and ((s[i] == 1) or (s[i] == 2 and s[i+1] <= 6)):
                dp[i] += dp[i+2]
        
        return dp[0]

            
