from collections import defaultdict

class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(list)
        
        for n in nums:
            sumv = sum(int(d) for d in str(n))
            dic[sumv].append(n)
        
        rst = -1
        
        for array in dic.values():
            if len(array) >= 2:
                # array.sort(reverse=True)
                # rst = max(rst, array[0] + array[1])
                n1, n2 = self.find_largest_two(array)
                rst = max(rst, n1 + n2)
        
        return rst
    
    def find_largest_two(self, array):
        """
        find and return the largest two numbers in array.
        Time: O(n)
        """
        ## find n1 and its index
        n1 = max(array)
        i1 = array.index(n1)
        n2 = float('-inf')
        for i, v in enumerate(array):
            if i != i1:
                n2 = max(n2, v)

        return n1, n2