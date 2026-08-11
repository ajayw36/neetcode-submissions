class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        start = 0
        diff = [gas[i] - cost[i] for i in range(len(gas))]

        for i in range(len(diff)):
            total += diff[i]

            if total < 0:
                total = 0
                start = i + 1
        
        return start
            
            
            