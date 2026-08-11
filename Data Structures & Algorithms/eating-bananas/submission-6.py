class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            speed = (l + r) // 2
            count = 0
            for pile in piles:
                count += math.ceil(pile / speed)
            if count <= h:
                r = speed
            else:
                l = speed + 1
        
        return l