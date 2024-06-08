
def fn(n: int):
  for i in range(n):
    yield i # instead of return

for i in fn(4):
  print(i)