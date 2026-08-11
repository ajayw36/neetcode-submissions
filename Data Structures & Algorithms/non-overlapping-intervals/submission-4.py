class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = -float('inf')
        res = 0
        for start, end in intervals:
            if start < prevEnd:
                res += 1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end
        return res