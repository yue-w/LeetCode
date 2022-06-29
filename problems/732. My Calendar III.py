

from collections import defaultdict
class MyCalendarThree:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> int:
        """
        Time: O(nlogn)
        """
        self.cal.append((start, 1))
        self.cal.append((end, -1))
        
        curr = 0
        rst = 0
        self.cal.sort()
        for _, val in self.cal:
            curr += val
            rst = max(curr, rst)
        return rst    


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)