
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import random
def rand7():
    return random.randrange(1, 8)
class Solution:
    """
    Notes:
    Generate rand7() from rand10():
    call rand10(), if generate a number that is larger than 7, do it until 
    a number bgetween 0 and 6 is generated. The probability of generated a 
    number between 0 and 6 is 1/7. Prof:
    p(0 to 6) = (1/10) + (3/10 * (1/10 + (3/10 * (1/10 + ...))))
              = 1/10 + 3/10 * 1/10 + (3/10)^2 * 1/10 + (3/10)^3 * 1/10
              = 1/7

    think in base 7, when using two bits to represent numbers, 
    call rand7() twice to generate the two numbers.
    ab = (rand7(), rand7())
    then ab is uniformly distributed number from 0 to 49
    i.e., 00, 01, 02, ..., 10, 20, .....66 are equally distributed, or in base
    10, number from 0 to 48 are equally distributed.
    Thus, we call rand7() twice to generate a number between 0 to 49, 
    if the number is larger than 39, retry, otherwise, we module(%) it with 10.
    Expectation of times of calling rand7():
      (40/49) * 2 + 9/49 * (2 + (40/49) * 2 + 9/49 * (2 + (40/49) * 2 + 9/49 + (...)))
    = (40/49) * 2 * (1 + 9/49 + (9/49)^2 + (9/49)^3 + ...)
    = ...
    """
    def rand10(self):
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

