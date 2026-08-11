class Solution:
    def trap(self, height: List[int]) -> int:
        i, water = 1, 0

        while i < len(height) - 1:
            l, r = 0, len(height) - 1
            max_l, max_r = 0, 0
            
            while l < i:
                if height[l] > max_l:
                    max_l = height[l]
                l += 1
            while r > i:
                if height[r] > max_r:
                    max_r = height[r]
                r -= 1
            
            if min(max_l, max_r) - height[i] > 0:
                water += min(max_l, max_r) - height[i]

            i += 1

        
        return water

            


        

