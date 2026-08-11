class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, water = 0, len(height) - 1, 0
        max_l, max_r = height[l], height[r]

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                if min(max_l, max_r) - height[l] > 0:
                    water += min(max_l, max_r) - height[l]
            
            else:
                r -= 1
                max_r = max(max_r, height[r])
                if min(max_l, max_r) - height[r] > 0:
                    water += min(max_l, max_r) - height[r]
        
        return water

            


        

