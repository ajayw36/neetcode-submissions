class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in t:
            if ch not in counts:
                return False
            counts[ch] -= 1
            if counts[ch] == 0:
                counts.pop(ch)
        
        return not counts;