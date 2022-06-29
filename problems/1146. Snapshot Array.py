g

import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.array = [0 for _ in range(length)]
        self.changed = set()
        self.snap_id = 0
        self.history = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        self.changed.add(index)

    def snap(self) -> int:
        for index in self.changed:
            self.history[index].append((self.snap_id, self.array[index]))
        self.changed.clear()
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        ## use binary search to find the largest self.history[index][0] that 
        ## is smaller than or equal to snap_id 
        index_index = bisect.bisect_right(self.history[index], snap_id, key=lambda x: x[0]) 
        return self.history[index][index_index - 1][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)