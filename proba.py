from pgmpy.utils.compat_fns import argmax
def fn(i, j):
    yield (i, j)
    yield (i+1, j)
b = fn(2, 2)
for i in b:
    print(i)
