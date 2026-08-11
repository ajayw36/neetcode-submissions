import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        
        
        while l < r:
            m = (l + r) // 2
            hours = 0
            for x in piles:
                hours += math.ceil(x/m)
            
            if hours <= h:
                r = m
            elif hours > h:
                l = m + 1
        
        return l
            

