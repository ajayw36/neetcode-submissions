class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            cars.append((p, s))

        cars.sort(reverse = True)
        stack = []
        res = len(cars)

        for p, s in cars:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                res -= 1
            else:
                stack.append(time)
        
        return res
