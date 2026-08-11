class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        count1 = [0] * 26
        count2 = [0] * 26

        for ch in s1:
            count1[ord(ch) - ord('a')] += 1
        
        for i in range(len(s1) - 1):
            count2[ord(s2[i]) - ord('a')] += 1
        
        i, j = 0, len(s1) - 1
        while j < len(s2):
            count2[ord(s2[j]) - ord('a')] += 1
            if count1 == count2: return True
            count2[ord(s2[i]) - ord('a')] -= 1
            i += 1
            j += 1
            
            
        
        return False