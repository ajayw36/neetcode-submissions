class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for ch in s:
            if ch.isalnum():
                new_str += ch.lower()
        
        l = 0
        r = len(new_str) - 1

        while l < r:
            if new_str[l] != new_str[r]:
                return False
            l += 1
            r -= 1
            
        return True
        