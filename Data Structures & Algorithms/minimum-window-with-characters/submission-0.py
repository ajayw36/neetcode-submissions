class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        T = {}
        for ch in t:
            T[ch] = T.get(ch,0) + 1

        have = 0
        need = len(T)
        i = 0
        j = 0

        res = ''

        while j < len(s):
            if s[j] in T:
                window[s[j]] = window.get(s[j], 0) + 1
                if window[s[j]] == T[s[j]]:
                    have += 1
            
            while have == need:
                if j-i+1 < len(res) or res == '':
                    res = s[i:j+1]
                if s[i] in T:
                    window[s[i]] -= 1
                    if window[s[i]] < T[s[i]]:
                        have -= 1
                i += 1
            
            j += 1
        
        return res
            

        
                    



