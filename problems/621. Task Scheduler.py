

from collections import Counter
import heapq
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        return self.method1(tasks, n) # preferred method
        #return self.method2(tasks, n)
    def method1(self, tasks, n):
        """
        Heap
        """
        if n == 0:
            return len(tasks)
        counter = Counter(tasks)
        hq = []
        for _, val in counter.items():
            hq.append(-val)
        heapq.heapify(hq)
        rst = 0
        while hq:
            k = min(len(hq), n+1)
            tem = []
            for i in range(k):
                tem_most_common = heapq.heappop(hq)
                tem_most_common += 1
                if tem_most_common != 0:
                    tem.append(tem_most_common)
            if len(tem) > 0: 
                rst += n + 1
            else:
                rst += k
            for count in tem:
                heapq.heappush(hq, count)
        return rst
    
    def method2(self, tasks, n):
        """
        Trick. Reference: https://youtu.be/3DZE7cfgYyg 
        """
        counter = Counter(tasks)
        maxc = counter.most_common(1)[0][1]
        
        ## count the number of events with occurance equals most count
        tail = 0
        for count in counter.values():
            if count == maxc:
                tail += 1
        
        return max((n + 1)  * (maxc - 1) + tail, len(tasks))
        
                
            
if __name__ == '__main__':
    tasks = ["A","A","A","B","B","B"]
    n = 2
    # tasks = ["A","B","C","D","E","A","B","C","D","E"]
    # n = 4
    rst = Solution().leastInterval(tasks, n)

    print(rst)