class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have, need = 0, len(t)
        l, r = 0, 0
        res = s + ' '

        count_t = Counter(t)
        count_s = defaultdict(int)

        while r < len(s):
            ch = s[r]
            if ch in count_t:
                if count_s[ch] < count_t[ch]: have += 1
                count_s[ch] += 1
                
            while have == need:
                if len(s[l:r+1]) < len(res):
                    res = s[l:r+1]
                ch = s[l]
                if ch in count_t:
                    if count_t[ch] >= count_s[ch]: have -= 1
                    count_s[ch] -= 1
                l += 1

            r += 1
        
        return '' if len(res) == len(s) + 1 else res