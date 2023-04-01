
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        a = -1
        b = -1
        for inter in intervals:
            c, d = inter
            if c >= b:
                a = c
                b = d
            else:
                return False

        return True