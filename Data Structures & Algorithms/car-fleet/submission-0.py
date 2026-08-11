class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        
        cars.sort(reverse = True)

        fleet = len(cars)
        stack = []

        for car in cars:
            time = (target - car[0]) / car[1]
            if stack and time <= stack[-1]:
                fleet -= 1
            else:
                stack.append(time)        
        
        return fleet
            