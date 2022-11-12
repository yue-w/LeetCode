


class Solution:
    def countDigitOne(self, n: int) -> int:
        num = str(n)
        N = len(num)
        
        rst = 0
        
        ## 1 indexed from the first digit to the Nth digit (1 being the least significant digit)
        ## how many numbers that is not larger than n has a 1 at its ith digit
        for i in range(1, N+1):
            
            # group 1: the digit from i+1 to N are smaller than the corresponding digits of n
            # example: 
            # n =  3 4 5 8 7
            #          i
            # n' = 1 4 1 X X
            # then as long as the last 2 digits are smaller than 34, the final number is smaller than 34
            # in this case, there are 00 -> 33 of 34 cases. The first i - 1 digits can be any numbers
            
            rst += (n // (10 ** i)) * (10 ** (i- 1))
            
            
            # Group 2: the digit from i+1 to N equals to n's corresponding digits and the ith digit of n is larger than 1
            # example:
            # n =  3 4 3 8 7
            #          i
            # n' = 3 4 1 X X
            # The 1 to i-1'th digits can be any number
            
            if int(num[N - i]) > 1:
                rst += 10 ** (i-1)
            
            
            # Group 3: the digit from i+1 to N equals to n's corresponding digits and the ith digit is 1
            # example:
            # n =  3 4 1 8 7
            #          i
            # n' = 3 4 1 X X
            # The 1 to i-1'th digits can be any number that is smaller than 87
            
            elif int(num[N - i]) == 1:
                rst += n % (10 ** (i - 1)) + 1
                
            
            # Group 4: the ith digit is 0, no 1 is contributed, list it here just for completness
            
            else:
                rst += 0
                
        
        return rst

if __name__ == '__main__':
    n = 13
    rst = Solution().countDigitOne(n)
    print(rst)