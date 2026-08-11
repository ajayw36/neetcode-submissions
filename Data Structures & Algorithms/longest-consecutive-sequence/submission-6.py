class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0

        for num in nums:
            local_count = 1
            if num-1 not in nums:
                while num + 1 in nums:
                    local_count += 1
                    num += 1
                count = max(count, local_count)

        return count