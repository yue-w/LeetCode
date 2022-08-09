#%%
import bisect

array = [1,3,3,4]
print(bisect.bisect_left(array, 3))
print(bisect.bisect_right(array, 3))
# %%
from sortedcontainers import SortedList
a = SortedList([1,3,3,4])
print(a.bisect_left(3))
print(a.bisect_right(3))
# %%
