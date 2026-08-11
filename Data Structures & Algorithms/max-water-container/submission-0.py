class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            if area > most:
                most = area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return most
        