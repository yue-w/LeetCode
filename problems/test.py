

# %%
import heapq
hq = [(2, 3),(1, 2)]
a, b = heapq.heappop(hq)
print(a)
print(b)
# %%
left = float('-inf') 
right = float('inf') 
print(left + (right - left) // 2)
# %%
[1] + [] + [3]
# %%
a = [1,2,3]
a[:0] + [0] + a[0:]
# %%
a = [1,2,3]
a.sort()
print(a)
# %%
def factorial(n):
    if n == 0:
        return 1
    rst = 1
    while n > 0:
        rst *= n
        n -= 1
    return rst
print(factorial(10))
# %%
a = [1,2,3,4]
a.pop()
# %%
int('+4')
# %%
print(2**31)
# %%
a = ['a', 'b', 'cd', 'e']
print('/'.join(a))
# %%
9 % 3
# %%
