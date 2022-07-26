
#%%
def bit_count_one(n):
    print(f'binary: {bin(n)}')
    count = 0
    while n:
        count += 1
        n &= n - 1
    return count

bit_count_one(1234)
bit_count_one(0)
bit_count_one(4321)
bit_count_one(1)
bit_count_one(3654)


