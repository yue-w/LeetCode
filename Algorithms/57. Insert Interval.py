from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return self.method2(intervals, newInterval)
    
    
    def method1(self, intervals, newInterval):
        """
        Template method (sweeping line).
        Time: O(nlogn)
        Space: O(n)
        The following customerized sorting is used
        ## [1,1] and [1,0] is a tie on '1', by default, the one with smaller 
        ## second element come first.
        b = [[1,1],[2,1],[1,-1],[3,0]]
        b.sort()
        print(b)
        ## [1,1] and [1,0] is a tie on '1', we can change it to making the one with larger 
        ## second element come first.
        a = [[1,1],[2,1],[1,-1],[3,0]]
        a.sort(key=lambda x: (x[0], -x[1]))
        print(a).
        In the following case when a starting point overlap with an end point, 
        make sure the starting point comes first after sorting (to add 1 before subtract 1).
                    1            -1
                    |_____________|
                    
                        1                -1
                        |________________|
                        
                                         1             -1
                                         |_____________|
        """
        
        time_stamps = []
        for interval in intervals:
            time_stamps.append((interval[0], 1))
            time_stamps.append((interval[1], -1))
        
        time_stamps.append((newInterval[0], 1))
        time_stamps.append((newInterval[1], -1))
        
        ## Sort time_stamps. In a tie, put starting before ending ((x, 1) comes before (x, -1)) 
        time_stamps.sort(key = lambda x: [x[0], -x[1]])
        
        curr = 0
        rst = []
        for ts in time_stamps:
            if curr == 0 and curr + ts[1] > 0:
                start = ts[0]
            elif curr > 0 and curr + ts[1] == 0:
                end = ts[0]
                rst.append([start, end])
            curr += ts[1]
        return rst
    
    def method2(self, intervals, newInterval):
        """
        Normal method.
        Time: O(n)
        Space: O(1)
        """
        rst = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                rst.append(newInterval)
                return rst + intervals[i:]
            elif newInterval[0] > interval[1]:
                rst.append(interval)
            else:
                # merge
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        rst.append(newInterval)
        return rst
    

            

if __name__ == '__main__':
     intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
     newInterval = [4,8]
     rst = Solution().insert(intervals, newInterval)
     print(rst)