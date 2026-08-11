class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        
        for ch in s:
            if ch.isalnum():
                new_str += ch.lower()

        start, end = 0, len(new_str) - 1

        while start < end:

            if new_str[start] != new_str[end]:
                return False
            
            start += 1
            end -= 1
        
        return True