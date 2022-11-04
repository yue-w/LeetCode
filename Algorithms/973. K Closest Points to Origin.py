from typing import List
import random
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #return self.method1(points, k)
        #return self.method2(points, k)
        return self.method3(points, k)
    
    def method1(self, points, k):
        """
        Quick select
        TIme: O(n) on average.
        """
        if len(points) <= k:
            return points
        #### step 1: preprocess
        dis2 = [0] * len(points)
        for i, (x, y) in enumerate(points):
            dis2[i] = x*x + y*y
        
        def quick_select(start, end):
            ## base case
            if len(rst) == k:
                return
            """
            intermediate state:
            S S S S S S S E E E E E U U U U L L L L L L 
            |             |         |     |           |
           start         left      curr  right       end
            final state:
            S S S S S S S E E E E E L L L L L L L L L L 
            |             |         |                 |
           start         left      curr              end  
            """
            ## swap to randomnize
            rand_idx = random.randrange(start, end+1)
            dis2[start], dis2[rand_idx] = dis2[rand_idx], dis2[start]
            points[start], points[rand_idx] = points[rand_idx], points[start]
            
            pivot = dis2[start]
            ## partition
            left = curr = start
            right = end
            while curr <= right:
                if dis2[curr] < pivot:
                    dis2[left], dis2[curr] = dis2[curr], dis2[left]
                    points[left], points[curr] = points[curr], points[left]
                    left += 1
                    curr += 1
                elif dis2[curr] == pivot:
                    curr += 1
                else:
                    dis2[curr], dis2[right] = dis2[right], dis2[curr]
                    points[curr], points[right] = points[right], points[curr]
                    right -= 1

            
            ## recursion
            #if curr - 1 - start + 1 <= need:
            need = k - len(rst)
            if left - 1 - start + 1 > need:
                quick_select(start, left - 1)
            else:
                i = start
                while i < curr and len(rst) < k:
                    rst.append(points[i])
                    i += 1
                quick_select(i, end)

        rst = []
        quick_select(0, len(dis2)-1)
        return rst
        
    def method2(self, points, k):
        """
        Binary search
        Time: O(nlogC)
        """
        def count_not_larger(dis2, val):
            """
            Return the count of points with dis2 value not larger than val
            """
            count = 0
            for m in dis2:
                if m <= val:
                    count += 1

            return count
        #### step 1: preprocess
        dis2 = [0] * len(points)
        for i, (x, y) in enumerate(points):
            dis2[i] = x*x + y*y
        
        left = min(dis2)
        right = max(dis2)
        
        while left < right:
            mid = left + (right - left) // 2
            count = count_not_larger(dis2, mid)
            if count >= k:
                right = mid
            else:
                left = mid + 1
                
        rst = []
        for i in range(len(points)):
            if dis2[i] <= left:
                rst.append(points[i])
        return rst
                
    def method3(self, points, k):
        """
        Heap.
        Time O(nlogk)
        """
        import heapq
        dis2 = [0] * len(points)
        for i, (x, y) in enumerate(points):
            dis2[i] = - (x*x + y*y)
        
        hq = []
        i = 0
        while i < k:
            hq.append((dis2[i], i))
            i += 1
        heapq.heapify(hq)
        for j in range(i, len(dis2)):
            v = dis2[j]
            if v > hq[0][0]:
                heapq.heappushpop(hq, (v, j))
        rst = []        
        for _, i in hq:
            rst.append(points[i])
        return rst
        

if __name__ == '__main__':
    points = [[3,3],[5,-1],[1,3]]
    k = 2
    rst = Solution().kClosest(points, k)
    print(rst)
