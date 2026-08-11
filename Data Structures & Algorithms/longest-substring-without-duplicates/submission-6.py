class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i, j = 0, 0
        res = 0

        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            res = max(res, j - i + 1)
            j += 1
    
        return res
