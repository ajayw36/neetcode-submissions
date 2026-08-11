class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = j = max_window = 0
        counts = [0] * 26

        while j < len(s):
            counts[ord(s[j]) - 65] += 1
            window_size = j - i + 1
            if window_size - max(counts) <= k:
                max_window = max(window_size, max_window)
            else:
                counts[ord(s[i]) - 65] -= 1
                i += 1
            j += 1
        return max_window
                

