from typing import List

class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        """
        Reference: https://youtu.be/66pxL0zkDUg
        """
        def bit_count_one(n: int) -> int:
            """
            Hanning mask, count how many bits are 1
            """
            count = 0
            while n:
                count += 1
                n &= n - 1
            return count
            
        m = len(mat)
        n = len(mat[0])
        upper_bnd = 2 ** n

        rst = 0
        # cast each row to an integer
        rows = [0] * m
        for r in range(m):
            number = ['0', 'b'] + [str(num) for num in mat[r]]
            number = ''.join(number)
            number = int(number, 2)
            rows[r] = number

        for c in range(upper_bnd):
            if bit_count_one(c) != cols:
                continue
            
            curr = 0
            for r in range(m):
                if (rows[r] & c) == rows[r]:
                    curr += 1
            
            rst = max(rst, curr)
        return rst