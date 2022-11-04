
from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_idx = [(heights[i], i) for i in range(len(heights))]
        heights_idx.sort(reverse=True)
        rst = []
        for _, i in heights_idx:
            rst.append(names[i])
        return rst