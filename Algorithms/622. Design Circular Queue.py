

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.head = 0 
        self.tail = -1
        self.length = 0
        
    def enQueue(self, value: int) -> bool:
        if self.length < self.k:
            self.length += 1
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = value
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.length > 0:
            self.length -= 1
            self.head = (self.head + 1) % self.k
            
            return True
        else:
            return False

    def Front(self) -> int:
        if self.length == 0:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.length == 0:
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.k