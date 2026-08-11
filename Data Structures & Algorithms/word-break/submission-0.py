class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
    # dp[i] is True/False whether the first i characters of s can be broken into words, so s[:i+1]. Iterate from i = 1 to n

        for i in range(1, n + 1):
            found = False
            for word in wordDict:
                if len(word) <= i and dp[i - len(word)] and s[i-len(word):i] == word:
                    found = True
                    break
            dp[i] = found
        
        print(dp)
        return dp[n]