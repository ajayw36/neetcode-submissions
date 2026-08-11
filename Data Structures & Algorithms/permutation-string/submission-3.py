class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counts1 = [0] * 26
        for ch in s1:
            counts1[ord(ch) - 97] += 1

        counts2 = [0] * 26
        i = 0
        j = len(s1) - 1

        for k in range(j):
            counts2[ord(s2[k]) - 97] += 1

        while j < len(s2):
            
            counts2[ord(s2[j]) - 97] += 1

            if counts2 == counts1:
                return True
            
            counts2[ord(s2[i]) - 97] -= 1
            
            j += 1
            i += 1

    
        return False