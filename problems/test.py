
#%%
array = [[1,2,3,4],[5,6,7,8],[9, 10, 11, 12]]
array_T = list(map(list, zip(*array)))
print(array)
print(array_T)
# %%
array = [[1,2,3,4],[5,6,7,8],[9, 10, 11, 12]]
for a, b in zip(*array):
    print(a, b)
# %%
