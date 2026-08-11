class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        i = j = 0

        while j < len(nums):
            while q and nums[j] > q[-1][0]:
                q.pop()
            q.append((nums[j], j))

            if i > q[0][1]:
                q.popleft()

            if j >= k - 1:
                res.append(q[0][0])
                i += 1

            j += 1

        return res
            