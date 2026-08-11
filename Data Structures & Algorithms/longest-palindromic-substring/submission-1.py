# 2D DP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return ''

        n = len(s)
        memo = [[False] * n for _ in range(n)]
        for i in range(n):
            memo[i][i] = True
        
        res_len = 1
        res = s[0]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or memo[i+1][j-1]):
                    memo[i][j] = True
                    if j - i + 1 > res_len:
                        res_len = j - i + 1
                        res = s[i:j+1]

        return res

        
        