from typing import List
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        n1 = len(items1)
        n2 = len(items2)
        if n1 < n2:
            dic_items = items1
            check_items = items2
        else:
            dic_items = items2
            check_items = items1
        dic = {value:weight for value, weight in dic_items}
        ret = []
        for value, weight in check_items:
            if value in dic:
                ret.append([value, weight + dic[value]])
                del dic[value]
            else:
                ret.append([value, weight])
                
        for value, weight in dic.items():
            ret.append([value, weight])
        ret.sort()
        return ret