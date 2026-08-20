class Deque:
    
    def __init__(self):
        self.capacity = 4
        self.arr = [0] * 4
        self.front = 0
        self.back = 0
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0
    
    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_arr = [0] * new_capacity

        for i in range(self.size):
            new_arr[i] = self.arr[(self.front + i) % self.capacity]
        self.arr = new_arr
        self.capacity = new_capacity
        self.front = 0
        self.back = self.size

    def append(self, value: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.back] = value
        self.back = (self.back + 1) % self.capacity
        self.size += 1

    def appendleft(self, value: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.front = (self.front - 1) % self.capacity
        self.arr[self.front] = value
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        idx = (self.back - 1) % self.capacity
        val = self.arr[idx]
        self.back = idx
        self.size -= 1
        return val
        

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        
        val = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val
