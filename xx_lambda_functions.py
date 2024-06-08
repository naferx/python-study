#  lambda parameters: expression

sqr  = lambda x: x * x
two  = lambda: 2  # parameterless function

print(sqr(3))

ls  = [1, 2, 3, 4]
nls = list(map(lambda x: x + 1,  ls))

print(nls)

fl = list(filter(lambda x: x < 3, ls))
print(fl)