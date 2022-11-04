from typing import List
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        
        rst = 0
        n = len(energy)
        ## energy
        eng = initialEnergy
        for i in range(n):
            if eng > energy[i]:
                eng -= energy[i]
            else:
                e = energy[i] - eng + 1
                rst += e
                eng = 1
                
        
        ## experience
        exp = initialExperience 
        for i in range(n):
            if exp > experience[i]:
                exp += experience[i]
            else:
                h = experience[i] - exp + 1
                rst += h
                exp = experience[i] * 2  + 1 
        return rst
            
            