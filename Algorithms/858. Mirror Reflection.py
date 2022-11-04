import math
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        Reference: https://youtu.be/RB22pCOZFts
        gcd: greatest common divisor
        lcm: least common multiple
        """
        lcm = abs(p*q) / math.gcd(p, q)
        height = lcm
        ## even height/p hits 0, odd height/p hits 1 or 2
        if height/p % 2 == 0:
            return 0
        
        ## count of flip. Even flip hits left wall, odd flip hits right wall
        t_flip = height / q
        if t_flip % 2 == 0:
            return 2
        else:
            return 1
