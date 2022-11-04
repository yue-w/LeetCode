# - 3 AND 8 = 0.
# - 3 AND 48 = 0.
# - 8 AND 48 = 0.

#%%
from functools import cache
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

print(factorial(100))