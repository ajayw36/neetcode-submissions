class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        starts = []
        for num in nums:
            if num - 1 not in nums:
                starts.append(num)

        count = 0
        for start in starts:
            temp_count = 1
            while start + 1 in nums:
                start = start + 1
                temp_count += 1
            count = max(count, temp_count)

        return count