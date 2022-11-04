
from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        if '0000' == target:
            return 0
        dq = deque()
        string = ['0'] * 4
        dq.append(string)
        steps = 0
        visited = set(string)
        while dq:
            steps += 1
            for _ in range(len(dq)):
                stringcp = dq.popleft()
                for i in range(4):
                    for j in [-1, 1]:
                        string = stringcp[:]
                        string[i] = str((int(string[i]) + j + 10 ) % 10)
                        if ''.join(string) == target:
                            return steps
                        if ''.join(string) in deadends:
                            continue
                        if ''.join(string) in visited:
                            continue
                        visited.add(''.join(string))
                        dq.append(string)
        
        return -1
        
if __name__ == '__main__':
     deadends = ["0201","0101","0102","1212","2002"]
     target = "0202"
     rst = Solution().openLock(deadends,target)
     print(rst)

            
        
        