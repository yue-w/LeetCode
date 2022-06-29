
from readline import set_history_length
from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """
        dp[i]: total height of the shelf when book 1 to i is on the shelf.
        """
        N = len(books)
        dp = [float('inf') for _ in range(N + 1)]
        ## add a dummy book to make it 1 indexed
        books = [[0, 0]] + books
        dp[0] = 0
        for i in range(1, N+1):
            curh = 0 #books[i][0]
            curw = 0 #books[i][1]
            for j in range(i, 0, -1):
                curh = max(curh, books[j][1])
                curw += books[j][0]
                if curw > shelfWidth:
                    break
                dp[i] = min(dp[i], dp[j - 1] + curh)
                
        return dp[-1]
                
        
if __name__ =='__main__':
    # books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    # shelf_width = 4
    books = [[7,3],[8,7],[2,7],[2,5]]
    shelf_width = 10
    rst = Solution().minHeightShelves(books, shelf_width)
    print(rst)
        
"""

dp[i]: height of the shelf containing book i.

"""