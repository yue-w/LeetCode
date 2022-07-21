
#%%
from sortedcontainers import SortedList
# %%
table = [[] for _ in range(10)]
table[0].append(1)
array = table[1]
if not array:
    print("empty")

