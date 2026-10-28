class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(m):
            hours = h
            for pile in piles:
                hours -= math.ceil(pile / m)
            return hours >= 0
            

        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if canEat(m):
                r = m
            else:
                l = m + 1
        return l