class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.front = 0
        self.back = 0
        self.arr = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.arr[0] = value
            self.size += 1
            return True

        if self.size == self.capacity:
            return False

        self.back = (self.back + 1) % self.capacity
        self.arr[self.back] = value
        self.size += 1

        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.arr[self.front] = None
            self.size = 0
            return True

        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.arr[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.arr[self.back] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()