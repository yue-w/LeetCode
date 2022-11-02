
from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.booking = SortedList()
        

    def book(self, start: int, end: int) -> bool:
        ## if empty
        if not self.booking:
            self.booking.add((start, end))
            return True
        idx = self.booking.bisect_left((start, end))
        ## if to be inserted to index 0
        if idx == 0:
            if end <= self.booking[0][0]:
                self.booking.add((start, end))
                return True
            return False
        ## if to be inserted to the last index
        if idx == len(self.booking):
            if start >= self.booking[-1][1]:
                self.booking.add((start, end))
                return True
            return False
        ## if to be inserted in between
        if start >= self.booking[idx-1][1] and end <= self.booking[idx][0]:
            self.booking.add((start, end))
            return True
        else:
            return False
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

"""
Binary search
"""