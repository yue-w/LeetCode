


from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.dict1 = {}
        self.dict2 = {}        

    def change(self, index: int, number: int) -> None:
        if not index in self.dict1:
            self.dict1[index] = number
            if not number in self.dict2:
                self.dict2[number] = SortedSet()
            self.dict2[number].add(index) 
        else:
            orinum = self.dict1[index]
            if orinum == number:
                return
            self.dict1[index] = number
            ## update set for the new number
            if not number in self.dict2:
                self.dict2[number] = SortedSet()
            self.dict2[number].add(index)
            ## update set for orinum
            self.dict2[orinum].remove(index)
            if len(self.dict2[orinum]) == 0:
                del self.dict2[orinum]

    def find(self, number: int) -> int:
        if not (number in self.dict2):
            return -1
        return self.dict2[number][0]
            
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)