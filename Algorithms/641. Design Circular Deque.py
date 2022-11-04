

class MyCircularDeque:

    def __init__(self, k: int):
        self.cdq = [0] * k
        self.left = 0
        self.right = -1
        self.k = k
        self.total = 0
        

    def insertFront(self, value: int) -> bool:
        ## add from left then i -= 1
        if self.total == self.k:
            return False
        self.left -= 1
        if self.left < 0:
            self.left = self.k - 1
        self.cdq[self.left] = value
        self.total += 1
        return True

    def insertLast(self, value: int) -> bool:
        ## add from right then j += 1
        if self.total == self.k:
            return False
        self.right += 1
        if self.right >= self.k:
            self.right = 0
        self.cdq[self.right] = value
        self.total += 1
        return True
    
    def deleteFront(self) -> bool:
        if self.total == 0:
            return False
        
        self.left += 1
        if self.left == self.k:
            self.left = 0
        self.total -= 1
        return True

    def deleteLast(self) -> bool:
        if self.total == 0:
            return False
        
        self.right -= 1
        if self.right == -1:
            self.right = self.k - 1
        self.total -= 1
        return True 

    def getFront(self) -> int:
        if self.total == 0:
            return -1
        else:
            return self.cdq[self.left]

    def getRear(self) -> int:
        if self.total == 0:
            return -1
        else:
            return self.cdq[self.right]
        

    def isEmpty(self) -> bool:
        return self.total == 0

    def isFull(self) -> bool:
        return self.total == self.k


if __name__ == '__main__':

    obj = MyCircularDeque(3)
    param_1 = obj.insertLast(1)
    print(param_1)
    param_2 = obj.insertLast(2)
    print(param_2)
    param_3 = obj.insertFront(3)
    print(param_3)
    param_4 = obj.insertFront(4)
    print(param_4)
    param_5 = obj.getRear()
    print(param_5)
