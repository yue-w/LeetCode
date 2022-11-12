
from typing import List
from collections import Counter, defaultdict
import heapq

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        #return self.method1(nums)
        return self.method2(nums)
        
        
    def method1(self, nums):
        """
        Greedy + two hash
        Time: O(n)
        """
        ## remain is how many occurances remain 
        remain = Counter(nums)
        ## key is a sequence ending with "key" and with a length not smaller than 3, value is how many of such sequence are there
        found = defaultdict(int)
        
        for n in nums:
            if remain[n] == 0:
                continue
            ## if there is a sequence with length larger than or equal to 3 ends with nums[i] - 1, append nums[i] to it
            if found[n - 1] > 0:
                found[n] += 1
                found[n - 1] -= 1
                remain[n - 1] -= 1
                remain[n] -= 1
            ## else, nums[i] should be the first number of a sequence, need to find the following 2 other numbers, if cannot find them, return False
            else:
                ## whether there are nums[i] + 1 and nums[i] + 2 remain
                if remain[n + 1] > 0 and remain[n + 2] > 0:
                    found[n + 2] += 1
                    remain[n] -= 1
                    remain[n + 1] -= 1
                    remain[n + 2] -= 1
                else:
                    return False
        
        return True
    
    def method2(self, nums):
        """
        heap
        Time: O(nlogn)
        """
        ## heap. elements are tuples (first_element, second_element), first_element is the last element of the sequence, 
        ## second_element is the length of the sequence 
        hq = []
        
        for n in nums:
            ## if need to add an element into the heapq
            if not hq or hq[0][0] == n: 
                heapq.heappush(hq, (n, 1))
                continue
            
            ## if the new number cannot be added into the sequence
            while hq and hq[0][0] + 1 < n:
                _, count = heapq.heappop(hq)
                if count < 3:
                    return False
            
            ## when reaching this line, the heapq is either empty or we can append n to a sequence
            if hq:
                heapq.heapreplace(hq, (n, hq[0][1] + 1))
            else:
                heapq.heappush(hq, (n, 1))
                               
        ## check all element in heap has length larger or equal to 3
        while hq:
            _, length = heapq.heappop(hq)
            if length < 3:
                return False
        return True
        
if __name__ == '__main__':
    nums = [1,2,3,3,4,5]
    rst = Solution().isPossible(nums)
    print(rst)
