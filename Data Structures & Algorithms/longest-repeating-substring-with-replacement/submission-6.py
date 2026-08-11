class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = j = max_window = 0
        counts = [0] * 26

        while j < len(s):
            counts[ord(s[j]) - 65] += 1
            while j - i + 1 - max(counts) > k:
                counts[ord(s[i]) - 65] -= 1
                i += 1
            max_window = max(j - i + 1, max_window)  
            j += 1
        return max_window