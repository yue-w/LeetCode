

from collections import defaultdict
from sortedcontainers import SortedSet, SortedList
class NumberContainers:
    """
    #### Method 1: use SortedSet.
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

    def find(self, number: int) -> int:
        ## there may be empty set!
        if not (number in self.dict2) or len(self.dict2[number]) == 0:
            return -1
        return self.dict2[number][0]
    """

    #### Method 2: Use SortedList. Preferred method.
    def __init__(self):
        ## all unique numbers stored
        self.index_to_number = {}
        self.indexes = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            ## remove index from old_number
            self.indexes[old_number].remove(index)
        self.index_to_number[index] = number
        self.indexes[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.indexes or not self.indexes[number]:
            return -1
        else:
            return self.indexes[number][0]
        

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)