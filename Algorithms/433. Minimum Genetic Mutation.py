
from typing import List
from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        BFS
        """
        ## cast list to set
        bank = set(bank)
        
        ## corner case
        if not end in bank:
            return -1
        
        steps = -1
        dq = deque()
        curr = [s for s in start]
        dq.append(curr[:])
        visited = set()
        
        while dq:
            steps += 1
            for _ in range(len(dq)):
                currcp = dq.popleft()

                if ''.join(currcp) == end:
                    return steps
                if ''.join(currcp) in visited:
                    continue
                visited.add(''.join(currcp))
                
                for i in range(len(start)):
                    for c in ['A', 'C', 'G', 'T']:
                        curr = currcp[:]
                        if curr[i] == c:
                            continue
                        curr[i] = c
                        if not ''.join(curr) in bank:
                            continue
                        dq.append(curr)

        
        return -1
        
        
        
        
        