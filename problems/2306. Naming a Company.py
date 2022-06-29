  
from collections import List
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        return self.method2(ideas)
    
    def method1(self, ideas):
        """
        O(n^2)
        TLE and MLE
        """
        rst = 0
        seen = set(ideas)
        made = set()
        for i in range(len(ideas) - 1):
            for j in range(i + 1, len(ideas)):
                word1 = ideas[i]
                word2 = ideas[j]
                if word1[0] == word2[0]:
                    continue
                poten1 = word2[0] + word1[1:]
                poten2 = word1[0] + word2[1:]
                
                if (not poten1 in seen) and (not poten2 in seen): 
                    newword1 = poten1 + ' ' + poten2
                    if newword1 not in made:
                        rst += 1
                        made.add(newword1)
                    newword2 = poten2 + ' ' + poten1
                    if newword2 not in made:
                        rst += 1
                        made.add(newword2)                    
        return rst
    
    def method2(self, ideas):
        """
        Preferred method
        Time: O(n)
        Space: O(n)
        """
        sets = [set() for _ in range(26)]
        for word in ideas:
            index = ord(word[0]) - ord('a')
            sets[index].add(word[1:])
        
        rst = 0
        for i in range(0, 25):
            for j in range(i + 1, 26):
                ## use the built-in function intersection, or just iterate 
                ## the shorter set, see whether it is in the second set
                # common = sets[i].intersection(sets[j])
                # rst += 2 * (len(sets[i]) - len(common)) * (len(sets[j]) - len(common))
                common = 0
                for c1 in sets[i]:
                    if c1 in sets[j]:
                        common += 1
                rst += 2 * (len(sets[i]) - common) * (len(sets[j]) - common)
        
        
        return rst
        