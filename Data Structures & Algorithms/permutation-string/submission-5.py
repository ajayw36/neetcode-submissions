class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        s1_count = [0] * 26
        s2_count = [0] * 26

        for ch in s1:
            s1_count[ord(ch)-ord('a')] += 1

        i = 0
        for j in range(len(s2)):
            s2_count[ord(s2[j]) - ord('a')] += 1
            if s2_count == s1_count: return True
            while s2_count[ord(s2[j])-ord('a')] > s1_count[ord(s2[j])-ord('a')]:
                s2_count[ord(s2[i])-ord('a')] -= 1
                i += 1 

        return False
