class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, height in enumerate(heights):
            j = i
            while stack and height <= stack[-1][0]:
                old_height, j = stack.pop()
                res = max(res, (i - j) * old_height)
            stack.append((height, j))
        
        while stack:
            res = max(res, stack[-1][0] * (len(heights) - stack[-1][1]))
            stack.pop()
        
        return res