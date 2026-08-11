class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(rate):
            count = 0
            for pile in piles:
                if count > h: return False
                count += math.ceil(pile / rate)
            return count <= h

        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if can_eat(m):
                r = m
            else:
                l = m + 1
        return l
        