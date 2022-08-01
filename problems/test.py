
#%%
def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    ## remove space
    string = [char for char in s if char != ' ']
    s = ''.join(string)
    s = '+' + s
    stack = []
    i = 0
    while i < len(s):
        digit = []
        if s[i] == '+' or s[i] == '-':
            ope = s[i]
            i += 1
            while i < len(s) and s[i].isdigit():
                digit.append(s[i])
                i += 1
            if ope == '+':
                stack.append(int(''.join(digit)))
            else: #ope = '-'
                stack.append(-int(''.join(digit)))
        else: # * or /
            ope = s[i]
            i += 1
            while i < len(s) and s[i].isdigit():
                digit.append(s[i])
                i += 1
            if ope == '*':
                stack[-1] = stack[-1] * int(''.join(digit))
            else: # ope is '/'
                # print(stack[-1])
                # print(int(''.join(digit)))
                # print(int(-1.5))
                stack[-1] = int(stack[-1]/int(''.join(digit)))     
                #print(stack[-1] / int(''.join(digit)))

    return sum(stack)
print(calculate("14-3/2"))