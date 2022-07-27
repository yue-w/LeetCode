
#%%
def test():
    def fun():
        a.append(1)
    
    a = []
    fun()
    print(a)

test()

# %%
