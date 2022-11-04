  

from typing import List
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """
        NP hard problem. Use recursion to explort all possible solutions.
        Time: O(k^n) each bag of cookies have k possibilities.
        Space: O(n)
        Use binary search to (trim branches).
        """
        ## binary search
        left = 0
        right = sum(cookies)
        while left < right:
            ## how manu cookies have been asigned to each person
            allocated = [0] * k
            mid = left + (right - left) // 2
            ## if it is possible to use this strategy to get a result of mid,
            ## try smaller mid
            if self.dfs(cookies, k, mid, 0, allocated):
                right = mid
            ## else, the limit is too small, try larger result
            else:
                left = mid + 1
            
        return left
        
    def dfs(self, cookies, k, limit, cookie_i, allocated):
        ## base case
        if cookie_i == len(cookies):
            return True
        
        for i in range(k):
            ## if after geting this cookie, this person's cooke is smaller or equal
            ## to the limit, go further
            if allocated[i] + cookies[cookie_i] <= limit:
                allocated[i] += cookies[cookie_i]
                if self.dfs(cookies, k, limit, cookie_i + 1, allocated):
                    return True
                ## backiing track
                allocated[i] -= cookies[cookie_i]
        
        ## if none of the stratagies works, return False
        return False

if __name__ == '__main__':
    cookies = [8,15,10,20,8] 
    k = 2
    rst = Solution().distributeCookies(cookies, k)
    print(rst)