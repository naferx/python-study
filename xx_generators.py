
def fn(n: int):
  for i in range(n):
    yield i # instead of return

def power(n: int):
  p = 1
  for _ in range(n):
    yield p
    p *= 2


for i in fn(4):
  print(i)

for i in power(4):
  print(i)