class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pref = [0] * n
        suff = [0] * n
        cur_max = 0
        for i in range(1, n):
            if height[i-1] > cur_max:
                cur_max = height[i-1]
            pref[i] = cur_max
        cur_max = 0
        for i in range(n-2, 0, -1):
            if height[i+1] > cur_max:
                cur_max = height[i+1]
            suff[i] = cur_max

        res = 0
        for i in range(n):
            res += min(pref[i], suff[i]) - height[i] if min(pref[i], suff[i]) - height[i] > 0 else 0

        return res