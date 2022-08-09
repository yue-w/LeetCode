from typing import List

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        curr = 0
        earliest = {}
        for t in tasks:
            if t in earliest:
                curr = max(curr, earliest[t])
            earliest[t] = curr + space + 1
            curr += 1
        
        return curr