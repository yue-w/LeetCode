
class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = [[]]
        self.capacity = capacity
        ## self.left is the left most stack to push
        self.left = 0
        ## self.right is the right most stack to pop
        self.right = 0

    def push(self, val: int) -> None:
        if self.left == -1:
            self.stack.append([val])
        else:
            self.stacks[self.left].append(val)
        if len(stacks[self.left]) == self.capacity:
            self.update_left()
        

    def pop(self) -> int:
        if self.right == -1:
            return -1
        val = self.stacks[self.right].pop()
        self.update_right()
        
        return val
        
        

    def popAtStack(self, index: int) -> int:
        if len(self.stacks) <= index:
            return -1
        if not self.stacks[index]:
            return -1
        else:
            val = self.stack[index].pop()
            ## update self.left if necessary
            if self.left > index:
                self.left = index
            ## update self.right if necessary
            if not self.stack[index] and self.right == index:
                self.stacks.pop()
                self.right -= 1
            return val
    
    def update_left(self):
        """
        find the left most stack that has capacity
        """
        while self.left < len(self.stacks):
            if len(self.stacks[self.left]) == self.capacity:
                self.left += 1
            else:
                return
        if self.left == len(self.stacks):
            self.stacks.append([])
        
    def update_right(self):
        """
        find the right most stack that has element to pop
        """
        if not self.stacks[self.right]:
            self.stacks.pop()
            self.right -= 1
        while self.right >= 0:
            if self.stacks.[self.right]:
                return
            else:
                self.right -= 1
                
        
        
            
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)