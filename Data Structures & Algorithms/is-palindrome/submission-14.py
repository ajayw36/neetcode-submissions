class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for ch in s:
            if ch.isalnum():
                s2 += ch.lower()
        s = s2
        
        l, r = 0 , len(s) - 1        
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True