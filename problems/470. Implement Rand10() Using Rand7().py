
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import random
def rand7():
    return random.randrange(1, 8)
class Solution:
    def rand10(self):
        return self.method2()
    def method1(self):
        """
        My thoughts
        Call rand7() 2 times, first time determine first or second half,
        second time get value
        """
        num = 7
        while num == 7:
            num = rand7()
        
        firsthalf = (num % 2 == 1)
        
        val = 7
        while val == 6 or val == 7:
            val = rand7()
            
        if firsthalf:
            return val
        else:
            return val + 5

    def method2(self):
        """
        From Cracking the coding interview
        """
        num = 40
        while num > 39:
            ## base-6 two digit number
            digit2 = rand7() - 1 ## 0, 1, 2, 3, 4, 5, 6
            digit1 = rand7() - 1 ## 0, 1, 2, 3, 4, 5, 6
            num = digit2 * 7 + digit1
            
        val = (num % 10)
        return val + 1
        
if __name__ == '__main__':
    s = Solution()
    rst = s.rand10()
    print(rst)