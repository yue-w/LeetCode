from typing import  List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Am I allowed to change the values in citations? Sort it? If not, I may need to make a deep copy
        """
        citations.sort()
        print(citations)
        N = len(citations)
        rst = 0
        for i in range(-1, - N - 1, -1):
            citation = citations[i]
            count = abs(i)
            if count <= citation:
                rst = count
        
        return rst


if __name__ == '__main__':
    s = Solution()
    citations = [3,0,6,1,5]
    rst = s.hIndex(citations)
    print(rst)