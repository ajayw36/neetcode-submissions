class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, res = 0, 0, 0
        seen = set()
        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            res = max(res, len(seen))
            j += 1
        
        return res
                

            