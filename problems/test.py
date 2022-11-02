#%%
from typing import List

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        earliest_dic = {}
        rst = 0
        for i in range(len(tasks)):
            earliest = earliest_dic.get(tasks[i], rst)
            if earliest <= rst:
                rst += 1
            else:
                rst = earliest + 1
            earliest_dic[tasks[i]] = rst + space
        
        return rst

tasks = [1,2,1,2,3,1]
space = 3
rst = Solution().taskSchedulerII(tasks, space)
print(rst)