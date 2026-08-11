class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = s + ' '
        count_s = defaultdict(int)
        count_t = Counter(t)

        have = 0
        need = len(t)

        i = 0
        for j in range(len(s)):
            if count_s[s[j]] < count_t[s[j]]:
                have += 1
            count_s[s[j]] += 1
            
            while have == need:
                if len(s[i:j+1]) < len(res):
                    res = s[i:j+1]
                if count_s[s[i]] <= count_t[s[i]]:
                    have -= 1
                count_s[s[i]] -= 1
                i += 1
        
        if len(res) > len(s): return ''
        return res