from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return self.method1(gas, cost)
        
    def method1(self, gas, cost):
        """
        One trick to speep up: starting from i, if you run out of gas at index j,
        you cannot reach j from any points starting between i and j. So, if you
        start from i and end at j (j is not the destination), the next time, you 
        should search from j + 1.
        Time: O(n) 
        Space: O(n)
        This method is easier to understnand than method 2.  but longer codes.
        """
        if sum(gas) < sum(cost):
            return -1

        ## Double the array to simulate cycle.
        n = len(gas)
        for i in range(n):
            gas.append(gas[i])
        
        i = 0
        while i < n:
            curr = 0
            j = i
            while j < 2*n:
                if j == i + n:
                    return i
                if j < n:
                    gs = gas[j]
                    cst = cost[j] 
                else:
                    gs = gas[j - n]
                    cst = cost[j - n]
                curr += gs

                if curr >= cst:
                    curr = curr - cst                    
                    j += 1
                else:
                    if i == n - 1:
                        return -1
                    if j < n:
                        i = j + 1
                        break
                    else:
                        return -1

        return -1
        
if __name__ == '__main__':
    s = Solution()
    gas = [4,5,2,6,5,3]
    cost = [3,2,7,3,2,9]
    ans = s.canCompleteCircuit(gas, cost)
    print(ans)