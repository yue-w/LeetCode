

# %%
n = -12345
ans = 0
while n:
    ans = ans * 10 + n % 10
    n //= 10
print(ans)
# %%
a = [1,2]
c, d = a
# %%
a.pop()
# %%
a
# %%
a.sort(reverse=True)
# %%
a = 'a' + 'b'
# %%
a = a - 'b'
# %%
a = str('a')
# %%
a = 10
b = 1
if 0 < a < 11 and 0 < b < -2:
    print('True')
else:
    print('False')


# %%

6//2
# %%
(1,2) == (1,2)
# %%
a = [(1,2)]
a[0] == (1,2)
# %%
s = 'abcde'
len(s[-1: 0])
# %%
