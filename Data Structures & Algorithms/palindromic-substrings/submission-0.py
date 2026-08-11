class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = [[False] * n for _ in range(n)]
        res = 0

        # memo[i][j] = True if the substring from the i to the jth position
        # (Both inclusive) is a palindrome and false otherwise

        for i in range(n):
            memo[i][i] = True
        

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or memo[i+1][j-1]):
                    memo[i][j] = True
                    res += 1

        return res
