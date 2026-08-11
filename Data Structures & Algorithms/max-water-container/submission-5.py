class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            if heights[l] < heights[r]:
                new_area = heights[l] * (r - l)
                l += 1
            else:
                new_area = heights[r] * (r - l)
                r -= 1
            area = max(area, new_area)
            
        return area