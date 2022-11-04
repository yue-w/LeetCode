
import random 

class RandomizedSet:
    """
    self.nums_dic stores the number and its index in self.nums_list
    when deleting a number from self.nums_dic, get the index of the 
    number to be deleted, swap it with the last element in the list,
    then pop it. Maintain inforamtion of index in the whole process.
    """
    def __init__(self):
        self.dic = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            index = len(self.list)
            self.dic[val] = index
            self.list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            index = self.dic[val]
            last = self.list[-1]
            self.list[index] = last
            self.dic[last] = index
            del self.dic[val]
            self.list.pop()
            
            return True
        else:
            return False

    def getRandom(self) -> int:
        index = random.randrange(len(self.list))
        val = self.list[index]
        return val

if __name__ == '__main__':
    obj = RandomizedSet()
    print(obj.remove(0))
    print(obj.remove(0))
    print(obj.insert(0))
    print(obj.getRandom())
    print(obj.remove(0))
    print(obj.insert(0))