class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for ch in s:
            if ch.isalnum():
                new_str += ch.lower()
            
        i, j = 0, len(new_str) - 1

        while i < j:
            if new_str[i] != new_str[j]:
                return False
            i += 1
            j -= 1
        
        return True
        