class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = set()
        for ch in s:
            charset.add(ch)
        res = 0
        for ch in charset:
            count = 0  
            i = j = 0
            while j < len(s):
                if s[j] != ch:
                    count += 1
                while count > k:
                    if s[i] != ch:
                        count -= 1
                    i += 1
                res = max(res, j-i+1)
                j += 1


        return res