
#%%
from sortedcontainers import SortedList
# %%
sl = SortedList([1,3,2,4,5,2,3,1])
print(sl)
# %%
print(sl.bisect_left(10))

#%%
array = [[1,2,3],[4,5,6]]
array_T = list(map(list, zip(*array)))
print(array)
print(array_T)
# %%
array = [[1,2,3],[4,5,6]]
M = len(array)
N = len(array[0])
array_T = [[0 for _ in range(M)] for _ in range(N)]
for i in range(M):
    for j in range(N):
        array_T[j][i] = array[i][j]
print(array_T)
# %%
from collections import defaultdict
counter = defaultdict(int)
counter[0] += 2
counter.get(1, 0)
print(counter)
# %%
