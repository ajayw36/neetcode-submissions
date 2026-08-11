class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        array = []

        for num, frequency in frequencies.items():
            array.append([frequency, num])
        
        array.sort()

        res = []
        for i in range(k):
            res.append(array.pop()[1])

        return res