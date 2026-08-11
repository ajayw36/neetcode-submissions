class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        letters = set()

        while r < len(s):
            if s[r] not in letters:
                letters.add(s[r])
                longest = max(longest, r - l + 1)
                r += 1
            else:
                letters.remove(s[l])
                l += 1
        
        return longest