

# %%
a = [1,2,3,4]
b = [1,2,3,4]
print(a == b)

# %%
a = [1,2,3,4]
b = [1,2,3,4]
print(a == b)
# %%
7 >> 1
# %%
a = [1,2,3,4]
print(a[:-1])
# %%
(10 >> 3) & 1
# %%
import copy
a = [1,2,3,4]
def fun(a):
    b = a[:]
    b[0] = 111
    a = copy.deepcopy(b)
fun(a)
print(a)

# %%
